from heapq import *

class MedianFinder:
    
    def __init__(self):
        
        # our two heaps -- note: in python, the default is min heap,
        # so we have to negate the values in the 'max' heap to simulate
        # the expected behavior
        self.small, self.large = [], []
    
    # adds a number to the underlying heaps
    # if the length of both heaps is the same, we push the negative
    # of the number onto the small healp, the pop the small heap,
    # taking the negative of this pop value and pushing it onto large
    # alternatively, if the lengths are not the same, we push the raw 
    # value onto the large heap, then pop from large, taking the negative
    # and pushing it onto the small heap
    def addNum(self, num):
        if len(self.small) == len(self.large): heappush(self.large, -heappushpop(self.small, -num))
        else: heappush(self.small, -heappushpop(self.large, num))
    
    # this function is trivial and simply returns the median, which
    # now that we have two heaps, is quite easy to get. If the heaps
    # are the same length, we simply return the average of the first 
    # element from each heap. If the lengths are different, we return
    # the first element from large, since this is guarenteed to be the
    # middle element in this implementation
    def findMedian(self):
        if len(self.small) == len(self.large): return (self.large[0] - self.small[0]) / 2.0
        else: return float(self.large[0])