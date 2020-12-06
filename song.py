class song(object):## song object class

    def __init__(self, valence, year, acousticness, artists, danceability,## Song object constructor
                 duration_ms, energy, id, instrumentalness, key, liveness,
                 loudness, name, release_date, speechiness, tempo):

        self.valence = valence## Assigns valence
        self.year = year## Assigns year
        self.acousticness = acousticness## Assigns acousticness
        self.artists = artists## Assigns artists
        self.danceability = danceability## Assigns danceability
        self.duration_ms = duration_ms## Assigns duration_ms
        self.energy = energy## Assigns energy
        self.id = id## Assigns id
        self.instrumentalness = instrumentalness## Assigns instrumentalness
        self.key = key## Assigns key
        self.liveness = liveness## Assigns liveness
        self.loudness = loudness## Assigns loudness
        self.name = name## Assigns name
        self.release_date = release_date## Assigns release_date
        self.speechiness = speechiness## Assigns speechiness
        self.tempo = tempo## Assigns tempo
        self.score1 = 0.0## Intialize variables to hold the score 1
        self.score2 = 0.0## Intialize variables to hold the score 2
        self.score3 = 0.0## Intialize variables to hold the score 3

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
    