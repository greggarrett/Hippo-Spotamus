from song import song

class Node(song):
    #node is a song. Can rename to something better
    def __init__(self, node):
        super().__init__(node.valence, node.year, node.acousticness, node.artists, node.danceability,
                 node.duration_ms, node.energy, node.id, node.instrumentalness, node.key, node.liveness,
                 node.loudness, node.name, node.release_date, node.speechiness, node.tempo)
        self.adjacencyList = {}

    def getAdjacencyList(self):
        return self.adjacencyList.keys()

    def getWeight(self, adjacentNodeId):
        return self.adjacencyList[adjacentNodeId]

    def insertAdjacent(self, adjacentNodeId, weight):
        self.adjacencyList[adjacentNodeId] = weight

class Graph:
    def __init__(self):
        self.nodes = {}
        self.size = 0

    def insert(self, song):
        addedNode = Node(song)
        self.nodes[song.id] = addedNode
        self.size = self.size + 1

    def getNode(self, i):
        if i in self.nodes:
            return self.nodes[i]
        else:
            return None

    def insertWeight(self, fromSong, toSong, weight):
        if fromSong not in self.nodes or toSong not in self.nodes:
            self.insert(fromSong)
            self.insert(toSong)
        
        self.nodes[fromSong].insertAdjacent(toSong.id, weight)

    def listNodes(self):
        return self.nodes.keys()



#We will have to add BFS and stuff as well. This implementation may need tweakin
