class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        # the relative arrival times for each monster, sorted since we 
        # want to kill the one that is going to reach us first each turn
        arrivals = sorted([x / y for x, y in zip(dist, speed)])
        
        # remove the first one before the loop since we will always kill one
        # at time == 0
        arrivals.pop(0)

        # look through the arrival times and make sure that none of them arrive
        # before we would have been able to kill them
        # i.e., if the time that monster[i] arrives is less than i + 1
        # which is the next time we would be able to kill it, return i + 1
        for i, time in enumerate(arrivals):
            if time <= i + 1:
                return i + 1
            
        # if we didnt return earlier, we killed them all, so just return len(dist)
        return len(dist)