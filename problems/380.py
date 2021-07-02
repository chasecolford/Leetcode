import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.datamap = {}
        self.data = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.datamap: return False
        self.datamap[val] = len(self.data)
        self.data.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.datamap: return False
        
        # the only real trick to this entire problem is this:
        # we are going to move our current last item in our data array
        # to the location of the val that we want to remove, then simply pop
        # our data array, since this avoids having to shift everthing
        self.datamap[self.data[-1]] = self.datamap[val]
        self.data[self.datamap[val]] = self.data[-1]
        self.data.pop()
        self.datamap.pop(val)
        return True
    
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()