class song(object):

    def __init__(self, valence, year, acousticness, artists, danceability,
                 duration_ms, energy, id, instrumentalness, key, liveness,
                 loudness, name, release_date, speechiness, tempo):

        self.valence = valence
        #print("Valence", valence)
        self.year = year
        #print("Year", year)
        self.acousticness = acousticness
        #print("acousticness", acousticness)
        self.artists = artists
        #print("artists", artists)
        self.danceability = danceability
        #print("danceability", danceability)
        self.duration_ms = duration_ms
        #print("duration_ms", duration_ms)
        self.energy = energy
        #print("energy", energy)
        self.id = id
        #print("id", id)
        self.instrumentalness = instrumentalness
        #print("instrumentalness", instrumentalness)
        self.key = key
        #print("key", key)
        self.liveness = liveness
        #print("liveness", liveness)
        self.loudness = loudness
        #print("loudness", loudness)
        self.name = name
        #print("name", name)
        self.release_date = release_date
        #print("release_date", release_date)
        self.speechiness = speechiness
        #print("speechiness", speechiness)
        self.tempo = tempo
        #print("tempo", tempo, "\n")