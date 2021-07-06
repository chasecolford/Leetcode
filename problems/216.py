class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        
        # main backtracking function
        def backtrack(nums, k, target, path, res):
            if k < 0 or target < 0: return
            if k == 0 and target == 0: res.append(path[:])
            for i in range(len(nums)): backtrack(nums[i+1:], k-1, target - nums[i], path + [nums[i]], res)
        
        res = []
        backtrack(list(range(1,10)), k, target, [], res)
        return res