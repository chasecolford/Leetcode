class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        Probably best to think of this as finding cycles in directed graph.
        
        for exmaple: Input: 
        nums = [5,4,0,3,1,6,2]
        Output: 4
        nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
        nums[1] -> nums[4] -> nums[1] -> nums[4] ... is a cycle
        nums[3] -> nums[3] -> nums[3] -> nums[3] ... is a cycle
        nums[0] -> nums[5] -> nums[6] -> nums[2] ... is a cycle
        
        Is it possible to have a value that is not a cycle? we are given an array
        nums of length n where nums if a permutation of the numbers in the range [0, n-1].
        This means that every number in this range exists and is distinct, which also
        means that every 0-based index has a direct one-to-one mapping with a value
        somewhere in the array. This means that every single element is part of a cycle,
        where the max length cycle would be n (example: every element just points to
        the next, and the last points to the start), and the smallest cycle is of length
        0 (or 1?), as is seen with nums[3] in the above exmaple. 
        
        If we had an easy way to identify all of the unique cycles, it would be as simple
        as just taking the longest and returning it.
        
        Naive way would be to just follow each cycle and store each value seen in a set.
        Once we see the same value again, we know we are done and keep log the length of the cycle.
        If the length of this cycle is longer than our current longest, we can update that variable.
        
        We could try keeping a master set that logs all of the values we have seen, outside of the 
        temp set we use while following each cycle. This would help us avoid entering a cycle that 
        we have already identified from another starting location.
        """
        res, seen, curlen = 0, set(), 0
        
        # for each of the indexes in the nums array, attempt to follow their cycle        
        for i in range(len(nums)):
            
            cur = nums[i]
            # while we have not explored this node and its entire cycle
            while cur not in seen:
                seen.add(cur)
                cur = nums[cur]
                curlen += 1
                if curlen > res: res = curlen
                    
            curlen = 0
        
        return res
            