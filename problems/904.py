class Solution:
    def totalFruit(self, f: List[int]) -> int:
        """sliding window
        1. as long as we have only two types of fruit in our window,
            we will keep taking them
        2. when we find a new third fruit, we need to know how long ago
            we saw each of the fruits. We will always take the one we saw
            most recently, but we need to know how far back it went 
            before the other fruit ruined it since:
            "Once you reach a tree with fruit that cannot fit in your baskets, 
            you must stop."
        """
        n, taken, res, count = len(f), {}, 0, 0
        for r in range(n):
            
            # if we have less than two distinct fruits, or we have 2 and this fruit is one of them -> just take fruit
            if len(taken) < 2 or len(taken) == 2 and f[r] in taken:
                taken[f[r]] = r
                count += 1
            
            # if we have two distinct fruits and we are seeing a new one not in our map -> need to calculate
            elif len(taken) == 2 and f[r] not in taken: 
                
                # check each of the fruits we currently have, find which of them was last seen
                # then calculate how many occured since the least recently seen to adjust count
                recent = leastRecentIndex = recentCount = None
                a, b = taken.items()
                
                # find the most recently seen fruit
                recent = a[1] if a[1] == r-1 else b[1]
                
                # find the least recent fruits index
                leastRecentIndex = min(a[1], b[1])
                
                # calculate the count of consecutive recent fruits behind r
                recentCount = recent - leastRecentIndex
                
                # update count to remove the fruits outside of this recentCount range
                count = recentCount + 1
                
                # update taken
                taken.pop(f[leastRecentIndex])
                taken[f[r]] = r
                
            
            # update res
            res = max(res, count)
        
        return res