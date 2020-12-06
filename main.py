import csv
from song import song, songScore1Comparable, songScore2Comparable, songScore3Comparable
from scores import scores
from masterlist import masterlist
from minheap import minheap
from graph import Graph
from queue import PriorityQueue

with open("wakeup.txt", 'r') as file:
    print(file.read())

def keyChecker(dict, string):
    if string in dict.keys():
        return True
    else:
        return False

def idToName(id, songlist):
    for song in songlist:
        if (song.id == id):
            return song

    print("No song found with that ID")
    return

def nameSearch(name, songlist):
    found = []
    for song in songlist:
        if (song.name == name):
            found.append(song)

    return found

def getSongScore(dictionary, songID):
    for key in dictionary.keys():
        if key == songID:
            return dictionary[key]

def getSongScore1(s):
    return s.score1

def getSongScore2(s):
    return s.score2

def getSongScore3(s):
    return s.score3


songlist = [] #Declares as a list
with open('data.csv', 'r', encoding = 'utf-8', errors = 'ignore') as csvfile:# This works, don't question it
    reader = csv.reader(csvfile, delimiter=',')
    counter = 0 # Counter to exclude first row
    for row in reader:
      if counter > 0:
          songlist.append(song(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[8], row[9], row[10], row[11],
                          row[12], row[14], row[16], row[17], row[18]))# Assignment operator
          counter += 1
      else:
          counter +=1


#for song in songlist:# How to traverse songlist
    #print(song.name)

master = masterlist(songlist)# If we want an object for the list
scorelist = [] #declare a list
score1List = []
score2List = []
score3List = []

dictionary = {}
x = 0
size = len(songlist)
for song in songlist:
    song.score1 = s1 = (float(song.acousticness)+float(song.liveness))/2
    song.score2 = s2 = (float(song.valence) + float(song.danceability))/2
    song.score3 = s3 = (float(song.energy) + (float(song.tempo)/244))/2
    scorelist.append(scores(s1, s2, s3))
    score1List.append(song)
    score2List.append(song)
    score3List.append(song)
    dictionary[song.id] = [song]
    x = x + 1

score1List.sort(key=getSongScore1)
score2List.sort(key=getSongScore2)
score3List.sort(key=getSongScore3)

menu = True
while menu:
    print(
    "\n--------- MENU ---------\n"
    "1.Generate Max-Heap Playlist\n"
    "2.Generate Graph Playlist\n"
    "3.Search for Song ID\n"
    "4.Search Songs by Artist\n"
    "5.Exit\n"
    )
    menu = input("What would you like to do? ")
    if menu =="1":
        print("Heap")
        choice = input("Please enter a song: ")
        possible = []
        possible2 = []
        possibleSong = []
        targetSong = choice
        for song in songlist:
            if song.name == choice:
                possible.append(song.artists)
                possible2.append(song.id)
                possibleSong.append(song)
        if len(possible) == 0:
            print("Song not found, please try another song!")
        elif len(possible) == 1:
            targetSong = possibleSong[0]
            print("\n" + choice + " by " + possible[0] + '\n' + "has a songID of: " + possible2[0] + '\n')
        elif len(possible) > 1:
            print("Select the artist you are looking for: ")
            x = 1
            for artists in possible:
                print(str(x) + ': ' + artists)
                x = x + 1
            pick = input("Enter choice as a numerical answer ex '1' : ")
            targetSong = possibleSong[int(pick)-1]
            print("\n" + choice + " by " + possible[int(pick)-1] + '\n' + "has a songID of: " + possible2[int(pick)-1])

            # THIS IS THE PROBLEM AREA
            # Trying to get score object from dictionary given ID. Also want the song object
            # Can I just get a single key's pair from the dictionary and use that? How would I implement that?
            # Using the getSongScore method at the top

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



        print("\nPrinting First Playlist: ")
        print("---------------------------")
        #for resulting in resulting1:
           # print(resulting.name + " by " + resulting.artists)
        counter1 = 0
        for resulting in resulting1:
            if (counter1 < 15):
                print(resulting.name + " by " + resulting.artists)
                counter1 += 1

        print("\nPrinting Second Playlist: ")
        print("---------------------------")
        #for resulting in resulting2:
           # print(resulting.name + " by " + resulting.artists)
        counter2 = 0
        for resulting in resulting2:
            if (counter2 < 15):
                print(resulting.name + " by " + resulting.artists)
                counter2 += 1

        print("\nPrinting Third Playlist: ")
        print("---------------------------")

        counter = 0
        for resulting in resulting3:
            if (counter < 15):
                print(resulting.name + " by " + resulting.artists)
                counter += 1


        print("\nPrinting Final Playlist: ")
        print("---------------------------")
        for song in finalPlaylist:
            print(song.name + " by " + song.artists)


    elif menu =="2":
        print("Graph")
        choice = input("Please enter a song: ")
        possible = []
        possible2 = []
        possibleSong = []
        for song in songlist:
            if song.name == choice:
                possible.append(song.artists)
                possible2.append(song.id)
                possibleSong.append(song)
        if len(possible) == 0:
            print("Song not found, please try another song!")
        elif len(possible) == 1:
            targetSong = possibleSong[0]
            print("\n" + choice + " by " + possible[0] + '\n' + "has a songID of: " + possible2[0] + '\n')
        elif len(possible) > 1:
            print("Select the artist you are looking for: ")
            x = 1
            for artists in possible:
                print(str(x) + ': ' + artists)
                x = x + 1
            pick = input("Enter choice as a numerical answer ex '1' : ")
            targetSong = possibleSong[int(pick)-1]
            print("\n" + choice + " by " + possible[int(pick)-1] + '\n' + "has a songID of: " + possible2[int(pick)-1])

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
        for arts in artlist:
            print(arts)
    elif menu =="5":
      print("\nGoodbye!")
      menu = None
    else:
       print("Please Try Again")