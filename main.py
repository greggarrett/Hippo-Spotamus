import csv
from song import song
from scores import scores
from masterlist import masterlist
from minheap import minheap

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
dictionary = {}
x = 0
size = len(songlist)
for song in songlist:
    song.score1 = s1 = (float(song.acousticness)+float(song.liveness))/2
    song.score2 = s2 = (float(song.valence) + float(song.danceability))/2
    song.score3 = s3 = (float(song.energy) + (float(song.loudness)/-60))/2
    scorelist.append(scores(s1, s2, s3))
    dictionary[song.id] = [song]
    x = x + 1

menu = True
while menu:
    print(
    "\n--------- MENU ---------\n"
    "1.Generate Max-Heap Playlist\n"
    "2.Generate Graph Playlist\n"
    "3.Search for Song ID\n"
    "4.Exit\n"
    )
    menu = input("What would you like to do? ")
    if menu =="1":
        print("Heap")
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
            print(choice + " by " + possible[0] + '\n' + "has a songID of: " + possible2[0] + '\n')
        elif len(possible) > 1:
            print("Select the artist you are looking for: ")
            x = 1
            for artists in possible:
                print(str(x) + ': ' + artists)
                x = x + 1
            pick = input("Enter choice as a numerical answer ex '1' : ")
            if (pick <= len(possible)):
                print(choice + " by " + possible[int(pick)-1] + '\n' + "has a songID of: " + possible2[int(pick)-1])

            # THIS IS THE PROBLEM AREA
            # Trying to get score object from dictionary given ID. Also want the song object
            # Can I just get a single key's pair from the dictionary and use that? How would I implement that?
            # Using the getSongScore method at the top


        heap1 = minheap(len(songlist))
        heap2 = minheap(len(songlist))
        heap3 = minheap(len(songlist))

        for score in scorelist:
            heap1.insert(score.score1)
            heap2.insert(score.score2)
            heap3.insert(score.score3)

        resulting1 = []
        resulting2 = []
        resulting3 = []

        counter = 0
        while (counter < 15):
            resulting1.append(heap1.delete())
            resulting2.append(heap1.delete())
            resulting3.append(heap1.delete())
            counter += 1

        print("\nPrinting resulting1: ")
        for resulting in resulting1:
            print(resulting)

        print("\nPrinting resulting2: ")
        for resulting in resulting2:
            print(resulting)

        print("\nPrinting resulting3: ")
        for resulting in resulting3:
            print(resulting)

    elif menu =="2":
        print("Graph")
        choice = input("please enter a song: ")
        possible = []
        possible2 = []
        for song in songlist:
            if song.name == choice:
                possible.append(song.artists)
                possible2.append(song.id)
        if len(possible) == 0:
            print("Song not found, please try another song!")
        elif len(possible) == 1:
            print(choice + " by " + possible[0] + '\n' + "has a songID of: " + possible2[0] + '\n')
        elif len(possible) > 1:
            print("Select the artist you are looking for: ")
            x = 1
            for artists in possible:
                print(str(x) + ': ' + artists)
                x = x + 1
            pick = input("Enter choice as a numerical answer ex '1' : ")
            print('\n')
            print(possible2[int(pick) - 1])
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
      print("\nGoodbye!")
      menu = None
    else:
       print("Please Try Again")