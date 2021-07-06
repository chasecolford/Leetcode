class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        """
        
        """
        
        # main backtracking function
        def backtrack(path, target, start, res):
            
            # if target == 0, we have found a valid path that sums to target
            if target == 0:
                res.append(path[:])
                return
            
            # for each of the starting points from start to the end of nums
            for i in range(start, len(nums)):
                
                # if this is not the first index and num[i] == nums[i - 1]
                # we would be looking at a starting point with the same value,
                # which could lead to duplicates, so we skip these
                if i > start and nums[i] == nums[i - 1]: continue
                    
                # since the values are sorted, if this target - nums[i] is
                # already < 0, every number after num[i] will also be < 0
                if target - nums[i] < 0: break
                
                # add nums[i] to the path, increment the starting position (i + 1)
                # subtrack nums[i] from target
                backtrack(path + [nums[i]], target - nums[i], i + 1, res)
                
        res, path = [], []
        nums.sort() # this makes life easy by putting duplicate values side by side
        backtrack(path, target, 0, res)
        return res
        
    