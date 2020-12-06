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
        #intialize variables to hold the scores
        self.score1 = 0.0
        self.score2 = 0.0
        self.score3 = 0.0

#These may not be used anymore. Shall See
class songScore1Comparable(song):
    def __init__(self, s):
        super().__init__(s.valence, s.year, s.acousticness, s.artists, s.danceability,
                 s.duration_ms, s.energy, s.id, s.instrumentalness, s.key, s.liveness,
                 s.loudness, s.name, s.release_date, s.speechiness, s.tempo)

    def __gt__(self, other):
        return self.score1 > other.score1
    
    def __eq__(self, other):
        return self.score1 == other.score1 

class songScore2Comparable(song):
    def __init__(self, s):
        super().__init__(s.valence, s.year, s.acousticness, s.artists, s.danceability,
                 s.duration_ms, s.energy, s.id, s.instrumentalness, s.key, s.liveness,
                 s.loudness, s.name, s.release_date, s.speechiness, s.tempo)

    def __gt__(self, other):
        return self.score2 > other.score2
    
    def __eq__(self, other):
        return self.score2 == other.score2

class songScore3Comparable(song):
    def __init__(self, s):
        super().__init__(s.valence, s.year, s.acousticness, s.artists, s.danceability,
                 s.duration_ms, s.energy, s.id, s.instrumentalness, s.key, s.liveness,
                 s.loudness, s.name, s.release_date, s.speechiness, s.tempo)

    def __gt__(self, other):
        return self.score3 > other.score3
    
    def __eq__(self, other):
        return self.score3 == other.score3
    