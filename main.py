import pandas as pd
import numpy as nm
from song import song
from masterlist import masterlist


mydf = pd.read_csv('data.csv')
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',21)
#mydf.columns = mydf.columns.map(lambda capital: capital.capitalize())
print(mydf)
#print(mydf.info)


songlist = [(song(row.valence, row.year, row.acousticness, row.artists, row.danceability,
                 row.duration_ms, row.energy, row.id, row.instrumentalness, row.key, row.liveness,
                 row.loudness, row.name, row.release_date, row.speechiness, row.tempo))
            for index, row in mydf.iterrows()]

for x in range(len(songlist)):
    print (songlist[x].name)

#allSongs = masterlist(songlist)

#print(allSongs.songlist[song.name] for song in allSongs)