from song import song
from collections import deque

class Node(song):
    #node parameter below is a song. Can rename to something better
    def __init__(self, node):
        super().__init__(node.valence, node.year, node.acousticness, node.artists, node.danceability,
                 node.duration_ms, node.energy, node.id, node.instrumentalness, node.key, node.liveness,
                 node.loudness, node.name, node.release_date, node.speechiness, node.tempo)
        self.adjacencyList = {}
        self.visited = 0

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

    # fromSong and toSong are songs, edgeType is either:
    # <score1 = 0, >score1 = 1, <score2 = 2, >score2 = 3, <score3 = 4, >score3 = 5
    # Note that this disgusts me but I'll prob change later, just want it working rn
    def insertEdgeType(self, fromSong, toSong, edgeType):
        if fromSong not in self.nodes or toSong not in self.nodes:
            self.insert(fromSong)
            self.insert(toSong)
        
        self.nodes[fromSong.id].insertAdjacent(toSong.id, edgeType)

    def listNodes(self):
        return self.nodes.keys()

    #BFS Will run n times until numRepeats repeats are found
    def bfs(self, rootSong, numRepeats):
        q = deque([])
        outputList = []
        totalList = []
        q.append(self.getNode(rootSong.id))
        lastEdgeType = 0
        #avoidEdgeType = 0

        x = 1
        nodePosition = 0
        lastEdgeType = {}

        #This is the problem.

        while (numRepeats > 0):
            tempNode = q.pop()
            totalList.append(tempNode)
            if (nodePosition > 0):
                # was trying to use this to find what node this node came from
                if (lastEdgeType[nodePosition] % 2 == 0):
                    avoidEdgeType = lastEdgeType[nodePosition] + 1
                else:
                    avoidEdgeType = lastEdgeType[nodePosition] - 1

            #Basically, need to avoid going to previous edge. The equations above are based off of <score1 = 0, etc.
            #Was using visited bool but can't really do that because of double connected graph
            for adjacentNodeId in tempNode.getAdjacencyList():
                if (tempNode.adjacencyList[adjacentNodeId] != avoidEdgeType):
                    self.getNode(adjacentNodeId).visited = 1
                    q.append(self.getNode(adjacentNodeId))
                    if (totalList.__contains__(self.getNode(adjacentNodeId))):
                        outputList.append(self.getNode(adjacentNodeId))
                        numRepeats = numRepeats - 1
                lastEdgeType[x] = tempNode.adjacencyList[adjacentNodeId] 
                x = x + 1
            nodePosition = nodePosition + 1

            return outputList

        