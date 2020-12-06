from song import song
import sys
class minheap(object):

    def __init__(self, max):
        self.max = max
        self.size = 0
        self.heap = [0] * (self.max + 1)
        self.heap[0] = -1 * sys.maxsize

    def childLeft(self, loc):
        return 2 * loc

    def childRight(self, loc):
        return (2 * loc) + 1

    def parent(self, loc):
        return loc//2

    def heapifyDown(self, loc, score):
        if (score == 1):
            self.heapifyDown1(loc)
        elif (score == 2):
            self.heapifyDown2(loc)
        elif (score == 3):
            self.heapifyDown3(loc)

    def heapifyDown1(self, loc):
        if not (loc <= self.size and loc >= self.size//2):
            if (self.heap[loc] > self.heap[self.childLeft(loc)]) or (self.heap[loc] > self.heap[self.childRight(loc)]):
                if (self.heap[self.childLeft(loc)] < self.heap[self.childRight(loc)]):
                    self.heap[loc], self.heap[self.childLeft(loc)] = self.heap[self.childLeft(loc)], self.heap[loc]

                    self.heapifyDown1(self.childLeft(loc))
                else:
                    self.heap[loc], self.heap[self.childRight(loc)] = self.heap[self.childRight(loc)], self.heap[loc]

                    self.heapifyDown1(self.childRight(loc))


    def heapifyDown2(self, loc):
        if not (loc <= self.size and loc >= self.size//2):
            if (self.heap[loc] > self.heap[self.childLeft(loc)]) or (self.heap[loc] > self.heap[self.childRight(loc)]):
                if (self.heap[self.childLeft(loc)] < self.heap[self.childRight(loc)]):
                    self.heap[loc], self.heap[self.childLeft(loc)] = self.heap[self.childLeft(loc)], self.heap[loc]

                    self.heapifyDown2(self.childLeft(loc))
                else:
                    self.heap[loc], self.heap[self.childRight(loc)] = self.heap[self.childRight(loc)], self.heap[loc]

                    self.heapifyDown2(self.childRight(loc))


    def heapifyDown3(self, loc):
        if not (loc <= self.size and loc >= self.size//2):
            if (self.heap[loc] > self.heap[self.childLeft(loc)]) or (self.heap[loc] > self.heap[self.childRight(loc)]):
                if (self.heap[self.childLeft(loc)] < self.heap[self.childRight(loc)]):
                    self.heap[loc], self.heap[self.childLeft(loc)] = self.heap[self.childLeft(loc)], self.heap[loc]

                    self.heapifyDown3(self.childLeft(loc))
                else:
                    self.heap[loc], self.heap[self.childRight(loc)] = self.heap[self.childRight(loc)], self.heap[loc]

                    self.heapifyDown3(self.childRight(loc))


    def insert(self, song, val):
        if self.size >= self.max:
            return
        else:
            self.size += 1
            self.heap[self.size] = song
            loc = self.size
            #print("loc: ", loc)
            #print("self.heap[loc]: ", self.heap[loc])
            #print("self.size: ", self.size)
            #print("self.heap[self.parent(loc)]: ", self.heap[self.parent(loc)])

            if (val == 1):
                while (self.heap[loc].score1 < self.heap[self.parent(loc)].score1):
                    self.heap[loc], self.heap[self.parent(loc)] = self.heap[self.parent(loc)], self.heap[loc]
                    loc = self.parent(loc)
            elif (val == 2):
                while (self.heap[loc] < self.heap[self.parent(loc)]):
                    self.heap[loc], self.heap[self.parent(loc)] = self.heap[self.parent(loc)], self.heap[loc]
                    loc = self.parent(loc)
            elif (val == 3):
                while (self.heap[loc] < self.heap[self.parent(loc)]):
                    self.heap[loc], self.heap[self.parent(loc)] = self.heap[self.parent(loc)], self.heap[loc]
                    loc = self.parent(loc)


    def delete(self):
        top = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heapifyDown(1)
        return top
