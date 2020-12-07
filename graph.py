from song import song
from collections import deque

class Node(song):
    #node parameter below is a song. Can rename to something better
    def __init__(self, node):
        super().__init__(node.valence, node.year, node.acousticness, node.artists, node.danceability,
                 node.duration_ms, node.energy, node.id, node.instrumentalness, node.key, node.liveness,
                 node.loudness, node.name, node.release_date, node.speechiness, node.tempo)
        self.adjacencyList = {}
        self.directionsToIds = {}
        self.visited = 0

    def getAdjacencyList(self):
        return self.adjacencyList.keys()

    def getAdjacencyListFull(self):
        return self.adjacencyList

    def getWeight(self, adjacentNodeId):
        return self.adjacencyList[adjacentNodeId]

    def insertAdjacent(self, adjacentNodeId, edgeType):
        self.adjacencyList[adjacentNodeId] = edgeType
        self.directionsToIds[edgeType] = adjacentNodeId

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

    # fromSong and toSong are songs, edgeType is either:
    # <score1 = 0, >score1 = 1, <score2 = 2, >score2 = 3, <score3 = 4, >score3 = 5
    def insertEdgeType(self, fromSong, toSong, edgeType):
        if fromSong.id not in self.nodes.keys():
            self.insert(fromSong)
        if toSong.id not in self.nodes.keys():
            self.insert(toSong)
        
        self.nodes[fromSong.id].insertAdjacent(toSong.id, edgeType)

    def listNodes(self):
        return self.nodes.keys()

    #BFS Will run n times until numRepeats repeats are found
    def bfs(self, rootSong, numRepeats):
        q = deque()
        previousDirections = deque()
        outputList = []

        q.append(self.getNode(rootSong.id))
        previousDirections.append(-1)

        while (numRepeats > 0):
            tempNode = q.popleft()
            prevDirection = previousDirections.popleft()
            if (prevDirection % 2 == 0): #Checking to make sure bfs doesn't go backwards do to 2 edges being between each vertice
                prevDirection = prevDirection + 1
            else:
                prevDirection = prevDirection - 1

            for adjacentNodeId in tempNode.getAdjacencyList():
                if (tempNode.adjacencyList[adjacentNodeId] != prevDirection):
                    self.getNode(adjacentNodeId).visited = self.getNode(adjacentNodeId).visited + 1
                    q.append(self.getNode(adjacentNodeId))
                    previousDirections.append(tempNode.adjacencyList[adjacentNodeId])
                    if (self.getNode(adjacentNodeId).visited == 3): #Looks to see if this vertice has been visited 3 times
                        outputList.append(self.getNode(adjacentNodeId))
                        numRepeats = numRepeats - 1
                        if (numRepeats == 0):
                            break

        return outputList