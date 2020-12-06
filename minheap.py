from song import song
import sys
class minheap(object):

    def __init__(self, max):
        self.max = max
        self.size = 0
        self.heap = [0] * (self.max + 1)
        self.heap2 = [0] * (self.max + 1)
        self.heap[0] = -1 * sys.maxsize

    def childLeft(self, loc):
        return 2 * loc

    def childRight(self, loc):
        return (2 * loc) + 1

    def parent(self, loc):
        return loc//2

    def swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]
        self.heap2[first], self.heap2[second] = self.heap2[second], self.heap2[first]


    def heapifyDown(self, loc):
        if not (loc <= self.size and loc >= self.size//2):
            if (self.heap[loc] > self.heap[self.childLeft(loc)]) or (self.heap[loc] > self.heap[self.childRight(loc)]):
                if (self.heap[self.childLeft(loc)] < self.heap[self.childRight(loc)]):
                    self.swap(loc, self.childLeft(loc))
                    self.heapifyDown(self.childLeft(loc))

                else:
                    self.swap(loc, self.childRight(loc))
                    self.heapifyDown(self.childRight(loc))


    def insert(self, score, song):
        if self.size >= self.max:
            return
        else:
            if (self.size == 0):
                self.size += 1
                self.heap[self.size] = score
                self.heap2[self.size] = song
                loc = self.size

            elif (self.size <= self.max):
                self.size += 1
                self.heap[self.size] = score
                self.heap2[self.size] = song
                loc = self.size

                scoreLoc = self.heap[loc]
                scorePar = self.heap[self.parent(loc)]

                while (scoreLoc < scorePar):
                    ##print("IN PRINT 1 ---- scoreLoc: " + str(scoreLoc) + " ----- scorePar: " + str(scorePar))
                    self.swap(loc, self.parent(loc))
                    loc = self.parent(loc)
                    scoreLoc = self.heap[loc]
                    scorePar = self.heap[self.parent(loc)]



    def delete(self):
        top = self.heap2[1]
        self.heap[1] = self.heap[self.size]
        self.heap2[1] = self.heap2[self.size]
        self.size -= 1
        self.heapifyDown(1)
        return top