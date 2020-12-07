import csv
from graph import Graph
from minheap import minheap
from scores import scores
from song import song
from time import perf_counter

with open("wakeup.txt", 'r') as file:  ## Prints out wakeup ascii
    print(file.read())

def keyChecker(dict, string):  ## Checks if a given key is in a dictionary
    if string in dict.keys():  ## If the string is a key
        return True  ## Return True
    else:
        return False  ## Return False

def idToName(id, songlist):  ## Given an id, return its song object
    for song in songlist:  ## Loop over songs in songlist
        if (song.id == id):  ## If song id matches given id
            return song  ## Return song
    print("No song found with that ID")  ## If no song found, print this
    return

def nameSearch(name, songlist):  ## Given a name, returns all songs with matching name
    found = []  ## Initialize a list of found songs
    for song in songlist:  ## Loop over songs in songlist
        if (song.name == name):  ## If the song name matches the given name, append to the list
            found.append(song)
    return found  ## Return list of found songs

def getSongScore(dictionary, songID):  ## Given a song's ID, return the value in the dictionary
    for key in dictionary.keys():  ## Loops over the number of keys in the dictionary
        if key == songID:  ## If the key matches the given song ID return it's value
            return dictionary[key]

def getSongScore1(s):  ## Getter for a song's score 1
    return s.score1

def getSongScore2(s):  ## Getter for a song's score 2
    return s.score2

def getSongScore3(s):  ## Getter for a song's score 3
    return s.score3

songlist = []  ## Declares a list for songs

with open('data.csv', 'r', encoding = 'utf-8', errors = 'ignore') as csvfile:  ## Opens CSV File
    reader = csv.reader(csvfile, delimiter=',')  ## Creates a reader for the CSV File
    counter = 0  ## Counter to exclude the header
    for row in reader:  ## Loop over all rows in CSV File
      if counter > 0:  ## If not the first row, put needed column information into the song object and append to song list
          songlist.append(song(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[8], row[9], row[10], row[11],
                          row[12], row[14], row[16], row[17], row[18]))
          counter += 1  ## Increment the row counter
      else:  ## If the first row
          counter +=1  ## Increment the row counter

scorelist = []  ## Declare a list for scores
score1List = []  ## Declare a list for score 1s
score2List = []  ## Declare a list for score 2s
score3List = []  ## Declare a list for score 3s

dictionary = {}  ## Create a dictionary with songID, song object key-value pairs
x = 0
size = len(songlist)
for song in songlist: ## Loops over number of songs in songlist
    song.score1 = s1 = (float(song.acousticness)+float(song.liveness))/2  ## Score 1 is the average of acousticness and liveness
    song.score2 = s2 = (float(song.valence) + float(song.danceability))/2  ## Score 2 is the average of valence and danceability
    song.score3 = s3 = (float(song.energy) + (float(song.tempo)/244))/2  ## Score 3 is the average of energy and adjusted tempo
    scorelist.append(scores(s1, s2, s3))  ## Create a list of score objects containing all scores
    score1List.append(song)  ## Append score 1 to score 1 list
    score2List.append(song)  ## Append score 2 to score 2 list
    score3List.append(song)  ## Append score 3 to score 3 list
    dictionary[song.id] = [song]  ## Pairs song id to song object in dictionary
    x = x + 1  ## Increments x

score1List.sort(key=getSongScore1)  ## Sorts dictionary
score2List.sort(key=getSongScore2)  ## Sorts dictionary
score3List.sort(key=getSongScore3)  ## Sorts dictionary

menu = True  ## Bool to keep menu running until exit
while menu:  ## While not exiting, loop menu
    print(  ## Menu Print
    "\n---------- MENU ----------\n"
    "1.Generate Min-Heap Playlist\n"
    "2.Generate Graph Playlist\n"
    "3.Generate Combined Playlist\n"
    "4.Search for Song ID\n"
    "5.Search Songs by Artist\n"
    "6.Exit\n"
    )
    menu = input("What would you like to do? ")
    if menu =="1":  ## If our input is 1, build a min-heap playlist
        print("You have selected: Min-Heap Playlist")
        choice = input("Please enter a song: ")  ## Input for song selection
        possible = []  ## List for all possible artists
        possible2 = []  ## List for all possible song ids
        possibleSong = []  ## List for all possible song objects
        targetSong = choice  ## Target song is our choice
        valid = False  ## Initializes validity check as false
        for song in songlist:  ## Loop over songs in songlist
            if song.name == choice:  ## If the song name matches our choice
                possible.append(song.artists)  ## Append that artist to the list of possible artist
                possible2.append(song.id)  ## Append that id to the list of possible ids
                possibleSong.append(song)  ## Append that song to the list of possible songs
        if len(possible) == 0:  ## If no possible songs found
            print("Song not found, please try another song!")
            valid = False  ## Validity check is still false
        elif len(possible) == 1:  ## If only one possible song was found
            targetSong = possibleSong[0]  ## This must be our target song
            print("\nNow generating your recommended playlist. . .")
            valid = True  ## Validity check is true
        elif len(possible) > 1:  ## If multiple possible songs were found
            valid = True  ## Validity check is true
            print("Select the artist you are looking for: ")
            x = 1  ## Initializes x as 1
            for artists in possible: ## Loops over artists in list of potential artists
                print(str(x) + ': ' + artists)  ## Prints out option choice
                x = x + 1  ## Increments x
            pick = input("Enter choice as a numerical answer ex '1': ")  ## Prompts input for choosing which artist
            targetSong = possibleSong[int(pick)-1]  ## targetSong is the song by selected artist
            print("\nNow generating your recommended playlist. . .")

        if valid:  ## If validity check is true
            tstart = perf_counter()
            adjustedSongList = []  ## Make a playlist of song objects with adjusted scores
            for song in songlist:  ## Loop over songs in songlist
                song2 = song  ## Copy songs in songlist to a new song object
                adjustedSongList.append(song2)  ## Add the new song object to a cloned, adjusted list

            targetScore1 = targetSong.score1  ## Uses our targetSong's score 1 as the ideal score 1
            targetScore2 = targetSong.score2  ## Uses our targetSong's score 2 as the ideal score 2
            targetScore3 = targetSong.score3  ## Uses our targetSong's score 3 as the ideal score 3

            for song in adjustedSongList:  ## Loops over songs in adjustedSongList
                song.score1 = (1 - abs(targetScore1 - song.score1))  ## adjustedSong's score 1 is assigned
                song.score2 = (1 - abs(targetScore2 - song.score2))  ## adjustedSong's score 2 is assigned
                song.score3 = (1 - abs(targetScore3 - song.score3))  ## adjustedSong's score 3 is assigned

            heap1 = minheap(len(adjustedSongList))  ## Create a minheap for score 1 with the size of the adjustedSongList
            heap2 = minheap(len(adjustedSongList))  ## Create a minheap for score 2 with the size of the adjustedSongList
            heap3 = minheap(len(adjustedSongList))  ## Create a minheap for score 3 with the size of the adjustedSongList

            for song in adjustedSongList:  ## For songs in adjustedSongList
                heap1.insert(song.score1, song)  ## Insert song score 1 and song object into heap
                heap2.insert(song.score2, song)  ## Insert song score 2 and song object into heap
                heap3.insert(song.score3, song)  ## Insert song score 3 and song object into heap

            resulting1 = []  ## Create a list for the song similarity using score 1
            resulting2 = []  ## Create a list for the song similarity using score 2
            resulting3 = []  ## Create a list for the song similarity using score 3

            counter = len(adjustedSongList) ## Counter is initially the size of the playlist
            while counter > 0:  ## Counter decrements until there are none left
                resulting1.append(heap1.delete())  ## Delete top of min-heap and return the song object that was deleted to score 1 list
                resulting2.append(heap2.delete())  ## Delete top of min-heap and return the song object that was deleted to score 2 list
                resulting3.append(heap3.delete())  ## Delete top of min-heap and return the song object that was deleted to score 3 list
                counter -= 1  ## Decrements counter

            resulting1.reverse()  ## Reverse list 1 to get in correct priority
            resulting2.reverse()  ## Reverse list 2 to get in correct priority
            resulting3.reverse()  ## Reverse list 3 to get in correct priority

            joinedResulting = resulting1 + resulting2 + resulting3  ## Join all three lists together

            occurences = {}  ## Create a dictionary for occurences
            finalPlaylist = []  ## Create a list for the final playlist

            for song in joinedResulting:  ## Loop over songs in the combined lists
                if not song.id in occurences.keys():  ## If this song id isn't in a dictionary yet
                    occurences[song.id] = 1  ## Initialize it's occurence count as 1
                else:  ## If this song id has been added to dictionary already
                    occurences[song.id] += 1  ## Increment it's occurence
                    if len(finalPlaylist) < 15:  ## If our total playlist is still less than 15 songs
                        if occurences[song.id] == 2:  ## If this is the second time that we've found this song in our list
                            finalPlaylist.append(song)  ## Add this song to the final playlist

            tstop = perf_counter()
            print("\nPrinting Final Playlist: ")
            print("---------------------------")
            for song in finalPlaylist:  ## Loop over the songs in our final playlist
                print(song.name + " by " + song.artists)  ## Print out the songs in our final playlist

            elapsed = tstop-tstart
            print("\nPlaylist generated in: " + str(elapsed) + " seconds")

    elif menu =="2":  ## If our input is 2, build a graph playlist
        print("You have selected: Graph Playlist")
        choice = input("Please enter a song: ")## Input for song selection
        possible = []## List for all possible artists
        possible2 = []## List for all possible song ids
        possibleSong = []## List for all possible song objects
        targetSong = choice## Target song is our choice
        valid = False## Initializes validity check as false
        for song in songlist:  ## Loop over songs in songlist
            if song.name == choice:  ## If the song name matches our choice
                possible.append(song.artists)  ## Append that artist to the list of possible artist
                possible2.append(song.id)  ## Append that id to the list of possible ids
                possibleSong.append(song)  ## Append that song to the list of possible songs
        if len(possible) == 0:  ## If no possible songs found
            print("Song not found, please try another song!")
            valid = False  ## Validity check is still false
        elif len(possible) == 1:  ## If only one possible song was found
            targetSong = possibleSong[0]  ## This must be our target song
            print("\nNow generating your recommended playlist. . .")
            valid = True  ## Validity check is true
        elif len(possible) > 1:  ## If multiple possible songs were found
            valid = True  ## Validity check is true
            print("Select the artist you are looking for: ")
            x = 1  ## Initializes x as 1
            for artists in possible:  ## Loops over artists in list of potential artists
                print(str(x) + ': ' + artists)  ## Prints out option choice
                x = x + 1  ## Increments x
            pick = input("Enter choice as a numerical answer ex '1': ")  ## Prompts input for choosing which artist
            targetSong = possibleSong[int(pick) - 1]  ## targetSong is the song by selected artist
            print("\nNow generating your recommended playlist. . .")

        if valid:
            tstart = perf_counter()
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

            output = graph.treatLikeATripleLinkedList(targetSong, 15) #This line should be changed if you want to try bfs, dfs, or lastVersion
            tstop = perf_counter()

            for resultingSong in output:
                print(resultingSong.name + " by " + resultingSong.artists)

            elapsed = tstop - tstart
            print("\nPlaylist generated in: " + str(elapsed) + " seconds")

    elif menu == "3":  ## If our input is 3, generate a combined playlist
        print("You have selected: Combined Playlist")
        choice = input("Please enter a song: ")  ## Input for song selection
        possible = []  ## List for all possible artists
        possible2 = []  ## List for all possible song ids
        possibleSong = []  ## List for all possible song objects
        targetSong = choice  ## Target song is our choice
        valid = False  ## Initializes validity check as false
        for song in songlist:  ## Loop over songs in songlist
            if song.name == choice:  ## If the song name matches our choice
                possible.append(song.artists)  ## Append that artist to the list of possible artist
                possible2.append(song.id)  ## Append that id to the list of possible ids
                possibleSong.append(song)  ## Append that song to the list of possible songs
        if len(possible) == 0:  ## If no possible songs found
            print("Song not found, please try another song!")
            valid = False  ## Validity check is still false
        elif len(possible) == 1:  ## If only one possible song was found
            targetSong = possibleSong[0]  ## This must be our target song
            print("\nNow generating your recommended playlist. . .")
            valid = True  ## Validity check is true
        elif len(possible) > 1:  ## If multiple possible songs were found
            valid = True  ## Validity check is true
            print("Select the artist you are looking for: ")
            x = 1  ## Initializes x as 1
            for artists in possible:  ## Loops over artists in list of potential artists
                print(str(x) + ': ' + artists)  ## Prints out option choice
                x = x + 1  ## Increments x
            pick = input("Enter choice as a numerical answer ex '1': ")  ## Prompts input for choosing which artist
            targetSong = possibleSong[int(pick) - 1]  ## targetSong is the song by selected artist
            print("\nNow generating your recommended playlist. . .")

            if valid:
                tstart = perf_counter()
                ##  Heap Implementation
                adjustedSongList = []  ## Make a playlist of song objects with adjusted scores
                for song in songlist:  ## Loop over songs in songlist
                    song2 = song  ## Copy songs in songlist to a new song object
                    adjustedSongList.append(song2)  ## Add the new song object to a cloned, adjusted list

                targetScore1 = targetSong.score1  ## Uses our targetSong's score 1 as the ideal score 1
                targetScore2 = targetSong.score2  ## Uses our targetSong's score 2 as the ideal score 2
                targetScore3 = targetSong.score3  ## Uses our targetSong's score 3 as the ideal score 3

                for song in adjustedSongList:  ## Loops over songs in adjustedSongList
                    song.score1 = (1 - abs(targetScore1 - song.score1))  ## adjustedSong's score 1 is assigned
                    song.score2 = (1 - abs(targetScore2 - song.score2))  ## adjustedSong's score 2 is assigned
                    song.score3 = (1 - abs(targetScore3 - song.score3))  ## adjustedSong's score 3 is assigned

                heap1 = minheap(
                    len(adjustedSongList))  ## Create a minheap for score 1 with the size of the adjustedSongList
                heap2 = minheap(
                    len(adjustedSongList))  ## Create a minheap for score 2 with the size of the adjustedSongList
                heap3 = minheap(
                    len(adjustedSongList))  ## Create a minheap for score 3 with the size of the adjustedSongList

                for song in adjustedSongList:  ## For songs in adjustedSongList
                    heap1.insert(song.score1, song)  ## Insert song score 1 and song object into heap
                    heap2.insert(song.score2, song)  ## Insert song score 2 and song object into heap
                    heap3.insert(song.score3, song)  ## Insert song score 3 and song object into heap

                resulting1 = []  ## Create a list for the song similarity using score 1
                resulting2 = []  ## Create a list for the song similarity using score 2
                resulting3 = []  ## Create a list for the song similarity using score 3

                counter = len(adjustedSongList)  ## Counter is initially the size of the playlist
                while counter > 0:  ## Counter decrements until there are none left
                    resulting1.append(
                        heap1.delete())  ## Delete top of min-heap and return the song object that was deleted to score 1 list
                    resulting2.append(
                        heap2.delete())  ## Delete top of min-heap and return the song object that was deleted to score 2 list
                    resulting3.append(
                        heap3.delete())  ## Delete top of min-heap and return the song object that was deleted to score 3 list
                    counter -= 1  ## Decrements counter

                resulting1.reverse()  ## Reverse list 1 to get in correct priority
                resulting2.reverse()  ## Reverse list 2 to get in correct priority
                resulting3.reverse()  ## Reverse list 3 to get in correct priority

                joinedResulting = resulting1 + resulting2 + resulting3  ## Join all three lists together

                occurences = {}  ## Create a dictionary for occurences
                finalPlaylist = []  ## Create a list for the final playlist

                for song in joinedResulting:  ## Loop over songs in the combined lists
                    if not song.id in occurences.keys():  ## If this song id isn't in a dictionary yet
                        occurences[song.id] = 1  ## Initialize it's occurence count as 1
                    else:  ## If this song id has been added to dictionary already
                        occurences[song.id] += 1  ## Increment it's occurence
                        if len(finalPlaylist) < 15:  ## If our total playlist is still less than 15 songs
                            if occurences[song.id] == 2:  ## If this is the second time that we've found this song in our list
                                finalPlaylist.append(song)  ## Add this song to the final playlist

                ##  Graph Implementation
                graph = Graph()
                x = 0
                firstScore1 = score1List[x]
                firstScore2 = score2List[x]
                firstScore3 = score3List[x]

                # creates graph, each node with 6 connections, nodes are doubly connected between each other
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

                output = graph.treatLikeATripleLinkedList(targetSong, 15)  # This line should be changed if you want to try bfs, dfs, or lastVersion
                tstop = perf_counter()

                print("\nPrinting Final Playlist: ")
                print("---------------------------")
                for song in finalPlaylist:  ## Loop over the songs in our final playlist
                    print(song.name + " by " + song.artists)  ## Print out the songs in our final playlist
                for resultingSong in output:
                    print(resultingSong.name + " by " + resultingSong.artists)

                elapsed = tstop - tstart
                print("\nPlaylist generated in: " + str(elapsed) + " seconds")

    elif menu =="4":  ## If our input is 4, search for a song ID
        choice = input("Please enter a song title: ")
        possible = []  ## Creates a list of possible song artists
        possible2 = []  ## Creates a list of possible song ids
        for song in songlist:  ## Loops over songs in songlist
            if song.name == choice:  ## If the name of the song matches our input
                possible.append(song.artists)  ## Append the artist to our possible artists list
                possible2.append(song.id)  ## Append the id to our possible id list
        if len(possible) == 0:  ## If there were no possible songs found
            print("Song not found, please try another song!")
        elif len(possible) == 1:  ## If only one possible song was found
            print(choice + " by " + possible[0] + '\n' + "has a songID of: " + possible2[0])
        elif len(possible) > 1:  ## If multiple possible songs were found
            print("Select the artist you are looking for: ")
            x = 1  ## Initialize x as 1
            for artists in possible:  ## Loop over the artists in possible artists list
                print(str(x) + ': ' + artists)  ## Prints out option choice
                x = x + 1  ## Increment x
            pick = input("Enter choice as a numerical answer ex '1' : ")  ## Prompts input for choosing which artist
            print('\n' + choice + " by " + possible[int(pick)-1] + '\n' + "has a songID of: " + possible2[int(pick)-1])  ## Prints song by selected artist

    elif menu =="5":  ## If our input is 5, search for songs by artist
        artlist = []  ## Create list for songs by artist
        art = input("Input your favorite artist: ")  ## Input for artist choice
        art = "['" + art + "']"  ## Formats search term for artist value
        for song in songlist:  ## Loop over songs in songlist
            if song.artists == art:  ## If the giver artist name matches song's artist
                artlist.append(song.name)  ## Add song to list by artist

        if len(artlist) > 0:  ## If songs by artist were found
            print("\nShowing results for " + art + " : ")
            print("---------------------------")
            for songs in artlist:  ## Loop over songs in artlist
                print(songs)  ## Print songs by artist
        else:  ## If no songs by artist were found, print message
            print("\nNo artists found by that name!")

    elif menu =="6":  ## If our input is 6, exit the program
      print("\nGoodbye!")
      menu = None  ## Quit menu

    else:  ## If our input is invalid, print error message
       print("\nInvalid entry, please try again!")