import csv
import pandas as pd
import numpy as nm
from song import song
from masterlist import masterlist
from window import Window


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

Window()

