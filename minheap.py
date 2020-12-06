from song import song
import sys
class minheap(object):  ## Minheap object class

    def __init__(self, max): ## Initialize min-heap
        self.max = max  ## Assigns a max minheap value
        self.size = 0  ## Assigns a current size value
        self.heap = [0] * (self.max + 1)  ## Heap that stores song scores
        self.heap2 = [0] * (self.max + 1) ## Heap that stores song objects

    def childLeft(self, loc):  ## Getter for the left child
        return 2 * loc

    def childRight(self, loc):  ## Getter for the right child
        return (2 * loc) + 1

    def parent(self, loc):  ## Getter for the parent
        return loc//2

    def swap(self, first, second):  ## Swap function to make code cleaner
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]  ## Swaps the score values
        self.heap2[first], self.heap2[second] = self.heap2[second], self.heap2[first]  ## Swaps the song values, mirroring score

    def heapifyDown(self, loc):  ## Heapify down function
        if not (loc <= self.size and loc >= self.size//2): ## If not a leaf node
            if (self.heap[loc] > self.heap[self.childLeft(loc)]) or (self.heap[loc] > self.heap[self.childRight(loc)]):  ## If we need to switch a value
                if (self.heap[self.childLeft(loc)] < self.heap[self.childRight(loc)]):  ## If left is smaller than right
                    if (self.childLeft(loc) < self.size):  ## If can swap
                        self.swap(loc, self.childLeft(loc))  ## Swap current and left
                        self.heapifyDown(self.childLeft(loc))  ## Recursively call to heapifyDown, using location of left child
                else:  ## If right is smaller than left
                    if (self.childRight(loc) < self.size):  ## If right is able to be swapped
                        self.swap(loc, self.childRight(loc))  ## Swap current and right
                        self.heapifyDown(self.childRight(loc))  ## Recursively call to heapifyDown, using location of right child

    def insert(self, score, song):  ## Insert function
        if self.size >= self.max:  ## If the heapsize is larger than max, return
            return
        else:  ## If heap size is less than max
            if (self.size == 0):  ## If there's nothing in the heap yet
                self.size += 1  ## Increment heap size
                self.heap[self.size] = score  ## Heap1 at this position is our score
                self.heap2[self.size] = song  ## Heap2 at this position is our song
                loc = self.size  ## Update current location

            elif (self.size <= self.max):  ## If the heap is not full
                self.size += 1  ## Increment heap size
                self.heap[self.size] = score  ## Heap1 at this position is our score
                self.heap2[self.size] = song  ## Heap2 at this position is our song
                loc = self.size  ## Update current location
                scoreLoc = self.heap[loc]  ## scoreLoc is the value of the score at this location
                scorePar = self.heap[self.parent(loc)]  ## scorePar is the value of the parent's socre at this location

                while (scoreLoc < scorePar):  ## If the location score is less than parent score
                    self.swap(loc, self.parent(loc))  ## Swap location and parent
                    loc = self.parent(loc)  ## Location is updated
                    scoreLoc = self.heap[loc]  ## scoreLoc is the value of the score at this location
                    scorePar = self.heap[self.parent(loc)]  ## scorePar is the value of the parent's socre at this location

    def delete(self):  ## Delete function
        top = self.heap2[1]  ## Top if the top song object
        self.heap[1] = self.heap[self.size]  ## Replace top heap with largest score
        self.heap2[1] = self.heap2[self.size]  ## Mirror score heap using song heap
        self.size -= 1  ## Decrement size of heaps
        self.heapifyDown(1)  ## Heapify down using top loc
        return top  ## Return the song object