import csv
from song import song, songScore1Comparable, songScore2Comparable, songScore3Comparable
from scores import scores
from minheap import minheap
from graph import Graph
from queue import PriorityQueue

with open("wakeup.txt", 'r') as file:## Prints out wakeup ascii
    print(file.read())

def keyChecker(dict, string):## Checks if a given key is in a dictionary
    if string in dict.keys():## If the string is a key
        return True## Return True
    else:
        return False## Return False

def idToName(id, songlist):## Given an id, return its song object
    for song in songlist:## Loop over songs in songlist
        if (song.id == id):## If song id matches given id
            return song## Return song
    print("No song found with that ID")## If no song found, print this
    return

def nameSearch(name, songlist):## Given a name, returns all songs with matching name
    found = []## Initialize a list of found songs
    for song in songlist:## Loop over songs in songlist
        if (song.name == name):## If the song name matches the given name, append to the list
            found.append(song)
    return found## Return list of found songs

def getSongScore(dictionary, songID):## Given a song's ID, return the value in the dictionary
    for key in dictionary.keys():## Loops over the number of keys in the dictionary
        if key == songID:## If the key matches the given song ID return it's value
            return dictionary[key]

def getSongScore1(s):## Getter for a song's score 1
    return s.score1

def getSongScore2(s):## Getter for a song's score 2
    return s.score2

def getSongScore3(s):## Getter for a song's score 3
    return s.score3

songlist = []## Declares a list for songs

with open('data.csv', 'r', encoding = 'utf-8', errors = 'ignore') as csvfile:## Opens CSV File
    reader = csv.reader(csvfile, delimiter=',')## Creates a reader for the CSV File
    counter = 0## Counter to exclude the header
    for row in reader:## Loop over all rows in CSV File
      if counter > 0:## If not the first row, put needed column information into the song object and append to song list
          songlist.append(song(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[8], row[9], row[10], row[11],
                          row[12], row[14], row[16], row[17], row[18]))
          counter += 1## Increment the row counter
      else:## If the first row
          counter +=1## Increment the row counter

scorelist = []## Declare a list for scores
score1List = []## Declare a list for score 1s
score2List = []## Declare a list for score 2s
score3List = []## Declare a list for score 3s

dictionary = {}## Create a dictionary with songID, song object key-value pairs
x = 0
size = len(songlist)
for song in songlist:## Loops over number of songs in songlist
    song.score1 = s1 = (float(song.acousticness)+float(song.liveness))/2## Score 1 is the average of acousticness and liveness
    song.score2 = s2 = (float(song.valence) + float(song.danceability))/2## Score 2 is the average of valence and danceability
    song.score3 = s3 = (float(song.energy) + (float(song.tempo)/244))/2## Score 3 is the average of energy and adjusted tempo
    scorelist.append(scores(s1, s2, s3))## Create a list of score objects containing all scores
    score1List.append(song)## Append score 1 to score 1 list
    score2List.append(song)## Append score 2 to score 2 list
    score3List.append(song)## Append score 3 to score 3 list
    dictionary[song.id] = [song]## Pairs song id to song object in dictionary
    x = x + 1## Increments x

score1List.sort(key=getSongScore1)## Sorts dictionary
score2List.sort(key=getSongScore2)## Sorts dictionary
score3List.sort(key=getSongScore3)## Sorts dictionary

menu = True## Bool to keep menu running until exit
while menu:## While not exiting, loop menu
    print(## Menu Print
    "\n--------- MENU ---------\n"
    "1.Generate Min-Heap Playlist\n"
    "2.Generate Graph Playlist\n"
    "3.Search for Song ID\n"
    "4.Search Songs by Artist\n"
    "5.Exit\n"
    )
    menu = input("What would you like to do? ")
    if menu =="1":## If our input is 1, build a min-heap playlist
        print("You have selected: Min-Heap Playlist")
        choice = input("Please enter a song: ")## Input for song selection
        possible = []## List for all possible artists
        possible2 = []## List for all possible song ids
        possibleSong = []## List for all possible song objects
        targetSong = choice## Target song is our choice
        valid = False
        for song in songlist:## Loop over songs in songlist
            if song.name == choice:## If the song name matches our choice
                possible.append(song.artists)## Append that artist to the list of possible artist
                possible2.append(song.id)## Append that id to the list of possible ids
                possibleSong.append(song)## Append that song to the list of possible songs
        if len(possible) == 0:## If not possible songs found
            print("Song not found, please try another song!")
            valid = False
        elif len(possible) == 1:
            targetSong = possibleSong[0]
            print("\nNow generating your recommended playlist. . .")
            valid = True
        elif len(possible) > 1:
            valid = True
            print("Select the artist you are looking for: ")
            x = 1
            for artists in possible:
                print(str(x) + ': ' + artists)
                x = x + 1
            pick = input("Enter choice as a numerical answer ex '1': ")
            targetSong = possibleSong[int(pick)-1]
            print("\nNow generating your recommended playlist. . .")

        if valid:
            adjustedSongList = []
            for song in songlist:
                song2 = song
                adjustedSongList.append(song2)

            targetScore1 = targetSong.score1
            targetScore2 = targetSong.score2
            targetScore3 = targetSong.score3

            for song in adjustedSongList:
                song.score1 = (1 - abs(targetScore1 - song.score1))
                song.score2 = (1 - abs(targetScore2 - song.score2))
                song.score3 = (1 - abs(targetScore3 - song.score3))

            heap1 = minheap(len(adjustedSongList))
            heap2 = minheap(len(adjustedSongList))
            heap3 = minheap(len(adjustedSongList))

            for song in adjustedSongList:
                heap1.insert(song.score1, song)
                heap2.insert(song.score2, song)
                heap3.insert(song.score3, song)

            resulting1 = []
            resulting2 = []
            resulting3 = []

            counter = len(adjustedSongList)
            while counter > 0:
                resulting1.append(heap1.delete())
                resulting2.append(heap2.delete())
                resulting3.append(heap3.delete())
                counter -= 1

            resulting1.reverse()
            resulting2.reverse()
            resulting3.reverse()

            joinedResulting = resulting1 + resulting2 + resulting3

            occurences = {}
            finalPlaylist = []

            for song in joinedResulting:
                if not song.id in occurences.keys():
                    occurences[song.id] = 1
                else:
                    occurences[song.id] += 1
                    if len(finalPlaylist) < 15:
                        if occurences[song.id] == 2:
                            finalPlaylist.append(song)

            print("\nPrinting Final Playlist: ")
            print("---------------------------")
            for song in finalPlaylist:
                print(song.name + " by " + song.artists)

    elif menu =="2":
        print("You have selected: Graph Playlist")
        choice = input("Please enter a song: ")
        possible = []
        possible2 = []
        possibleSong = []
        targetSong = choice  ## Target song is our choice
        valid = False
        for song in songlist:  ## Loop over songs in songlist
            if song.name == choice:  ## If the song name matches our choice
                possible.append(song.artists)  ## Append that artist to the list of possible artist
                possible2.append(song.id)  ## Append that id to the list of possible ids
                possibleSong.append(song)  ## Append that song to the list of possible songs
        if len(possible) == 0:  ## If not possible songs found
            print("Song not found, please try another song!")
            valid = False
        elif len(possible) == 1:
            targetSong = possibleSong[0]
            print("\nNow generating your recommended playlist. . .")
            valid = True
        elif len(possible) > 1:
            valid = True
            print("Select the artist you are looking for: ")
            x = 1
            for artists in possible:
                print(str(x) + ': ' + artists)
                x = x + 1
            pick = input("Enter choice as a numerical answer ex '1': ")
            targetSong = possibleSong[int(pick) - 1]
            print("\nNow generating your recommended playlist. . .")

        if valid:
            graph = Graph()
            x = 0
            firstScore1 = score1List[x]
            firstScore2 = score2List[x]
            firstScore3 = score3List[x]

            #creates graph, each node with 6 connections, nodes are doubly connected between each other
            while x < len(songlist) - 1:
                secondScore1 = score1List[x + 1]
                graph.insertEdgeType(secondScore1, firstScore1, 0)
                graph.insertEdgeType(firstScore1, secondScore1, 1)
                firstScore1 = secondScore1

                secondScore2 = score2List[x + 1]
                graph.insertEdgeType(secondScore2, firstScore2, 2)
                graph.insertEdgeType(firstScore2, secondScore2, 3)
                firstScore2 = secondScore2

                secondScore3 = score3List[x + 1]
                graph.insertEdgeType(secondScore3, firstScore3, 4)
                graph.insertEdgeType(firstScore3, secondScore3, 5)
                firstScore3 = secondScore3
                x = x + 1
        
            output = graph.bfs(targetSong, 15)
            for resultingSong in output:
                print(resultingSong.name + " by " + resultingSong.artists)

    elif menu =="3":
        choice = input("Please enter a song: ")
        possible = []
        possible2 = []
        for song in songlist:
            if song.name == choice:
                possible.append(song.artists)
                possible2.append(song.id)
        if len(possible) == 0:
            print("Song not found, please try another song!")
        elif len(possible) == 1:
            print(choice + " by " + possible[0] + '\n' + "has a songID of: " + possible2[0])
        elif len(possible) > 1:
            print("Select the artist you are looking for: ")
            x = 1
            for artists in possible:
                print(str(x) + ': ' + artists)
                x = x + 1
            pick = input("Enter choice as a numerical answer ex '1' : ")
            print('\n' + choice + " by " + possible[int(pick)-1] + '\n' + "has a songID of: " + possible2[int(pick)-1])

    elif menu =="4":
        artlist = []
        art = input("Input your favorite artist: ")
        art = "['" + art + "']"
        for song in songlist:
            if song.artists == art:
                artlist.append(song.name)

        if len(artlist) > 0:
            print("\nShowing results for " + art + " : ")
            print("---------------------------")
            for arts in artlist:
                print(arts)
        else:
            print("\nNo artists found by that name!")

    elif menu =="5":
      print("\nGoodbye!")
      menu = None

    else:
       print("Invalid entry, please try again!")