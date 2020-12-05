import csv
from song import song
from masterlist import masterlist
from minheap import minheap
#from window import Window

songlist = [] #Declares as a list
with open('data.csv', 'r', encoding = 'utf-8', errors = 'ignore') as csvfile:# This works, don't question it
    reader = csv.reader(csvfile, delimiter=',')
    counter = 0 # Counter to exclude first row
    for row in reader:
      if counter > 0:
            # valence, year, acousticness, artists, danceability,
            # duration_ms, energy, id, instrumentalness, key, liveness,
            # loudness, name, release_date, speechiness, tempo
          songlist.append(song(float(row[0]), int(row[1]), float(row[2]), row[3], float(row[4]), int(row[5]),
                               float(row[6]), row[8], float(row[9]), int(row[10]), float(row[11]),
                               float(row[12]), row[14], row[16], float(row[17]), float(row[18])))# Assignment operator
          counter += 1
      else:
          counter +=1
            
master = masterlist(songlist)# If we want an object for the list
#for song in songlist:# How to traverse songlist
    #print(song.duration_ms)

heapA = minheap(len(songlist))

for song in songlist:
    heapA.insert(song.duration_ms)

resultingA = []

counter = 0
while (counter < 15):
    resultingA.append(heapA.delete())
    counter += 1

for duration_ms in resultingA:
    print(duration_ms)

#Window()

