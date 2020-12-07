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
    # Note that this disgusts me but I'll prob change later, just want it working rn
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
            if (prevDirection % 2 == 0):
                prevDirection = prevDirection + 1
            else:
                prevDirection = prevDirection - 1

            for adjacentNodeId in tempNode.getAdjacencyList():
                if (tempNode.adjacencyList[adjacentNodeId] != prevDirection):
                    self.getNode(adjacentNodeId).visited = self.getNode(adjacentNodeId).visited + 1
                    q.append(self.getNode(adjacentNodeId))
                    previousDirections.append(tempNode.adjacencyList[adjacentNodeId])
                    if (self.getNode(adjacentNodeId).visited == 3): #Doing it this way in case we want songs that appear in all 3 lists, not just 2
                        outputList.append(self.getNode(adjacentNodeId))
                        numRepeats = numRepeats - 1
                        if (numRepeats == 0):
                            break

        return outputList

    def dfs(self, rootSong, numRepeats):
        q = deque()
        previousDirections = deque()
        outputList = []

        q.append(self.getNode(rootSong.id))
        previousDirections.append(-1)

        while (numRepeats > 0):
            tempNode = q.pop()
            prevDirection = previousDirections.pop()
            if (prevDirection % 2 == 0):
                prevDirection = prevDirection + 1
            else:
                prevDirection = prevDirection - 1

            for adjacentNodeId in tempNode.getAdjacencyList():
                if (tempNode.adjacencyList[adjacentNodeId] != prevDirection):
                    self.getNode(adjacentNodeId).visited = self.getNode(adjacentNodeId).visited + 1
                    q.append(self.getNode(adjacentNodeId))
                    previousDirections.append(tempNode.adjacencyList[adjacentNodeId])
                    if (self.getNode(adjacentNodeId).visited == 3): #Doing it this way in case we want songs that appear in all 3 lists, not just 2
                        outputList.append(self.getNode(adjacentNodeId))
                        numRepeats = numRepeats - 1
                        if (numRepeats == 0):
                            break

        return outputList

    def treatLikeATripleLinkedList(self, rootSong, numRepeats):
        outputList = []
        repeatVal = 3 #Will not work if greater than 3!
        
        left1 = self.getNode(self.getNode(rootSong.id).directionsToIds[0])
        right1 = self.getNode(self.getNode(rootSong.id).directionsToIds[1])
        left2 = self.getNode(self.getNode(rootSong.id).directionsToIds[2])
        right2 = self.getNode(self.getNode(rootSong.id).directionsToIds[3])
        left3 = self.getNode(self.getNode(rootSong.id).directionsToIds[4])
        right3 = self.getNode(self.getNode(rootSong.id).directionsToIds[5])

        #could have helper method and simplify this but not sure if we are keeping
        while numRepeats > 0:
            left1.visited = left1.visited + 1
            if (left1.visited >= repeatVal):
                outputList.append(left1)
                numRepeats = numRepeats - 1

            right1.visited = right1.visited + 1
            if (right1.visited >= repeatVal):
                outputList.append(right1)
                numRepeats = numRepeats - 1
            
            left2.visited = left2.visited + 1
            if (left2.visited >= repeatVal):
                outputList.append(left2)
                numRepeats = numRepeats - 1

            right2.visited = right2.visited + 1
            if (right2.visited >= repeatVal):
                outputList.append(right2)
                numRepeats = numRepeats - 1

            left3.visited = left3.visited + 1
            if (left3.visited >= repeatVal):
                outputList.append(left3)
                numRepeats = numRepeats - 1

            right3.visited = right3.visited + 1
            if (right3.visited >= repeatVal):
                outputList.append(right3)
                numRepeats = numRepeats - 1

            if 0 in left1.directionsToIds.keys():
                left1 = self.getNode(left1.directionsToIds.get(0))
            else: #Will just stop at this node and be here forever basically.
                left1.visited = 0
            
            if 1 in right1.directionsToIds.keys():
                right1 = self.getNode(right1.directionsToIds.get(1))
            else: 
                right1.visited = 0

            if 2 in left2.directionsToIds.keys():
                left2 = self.getNode(left2.directionsToIds.get(2))
            else: #Will just stop at this node and be here forever basically.
                left2.visited = 0
            
            if 3 in right2.directionsToIds.keys():
                right2 = self.getNode(right2.directionsToIds.get(3))
            else: 
                right2.visited = 0

            if 4 in left3.directionsToIds.keys():
                left3 = self.getNode(left3.directionsToIds.get(4))
            else: #Will just stop at this node and be here forever basically.
                left3.visited = 0
            
            if 5 in right3.directionsToIds.keys():
                right3 = self.getNode(right3.directionsToIds.get(5))
            else: 
                right3.visited = 0

        return outputList


