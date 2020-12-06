import csv
from song import song
from scores import scores
from masterlist import masterlist
from minheap import minheap

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
    s1 = (float(song.acousticness)+float(song.liveness))/2
    s2 = (float(song.valence) + float(song.danceability))/2
    s3 = (float(song.energy) + (float(song.loudness)/-60))/2
    scorelist.append(scores(s1, s2, s3))

    dictionary[song.id] = [song, scorelist[x]]
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
        # Call Graph class
    elif menu =="3":
      print("ID of Song is: ")
        # Call ID finder
    elif menu =="4":
      print("\nGoodbye!")
      menu = None
    else:
       print("Please Try Again")