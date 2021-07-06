class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        backtracking: two main conditions:
        if the sum we are currently looking at == target: append to res and backtrack
        elif the sum we are currently looking at > target: backtrack
        remember that for this version, we can use the same value more that once, 
        therefore, if the numbers we have are [2, 4, 5], we would start by adding
        2 as many times as we can before reaching target exactly, or exceeding it.
        we will implement this by sunbtracting each value instead, which means we will
        backtrack when the value passed - next value is below 0.
        """
        # main backtracking function
        def backtrack(target, path, start):
            if target < 0: return
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(target - candidates[i], path, i)
                path.pop()
                
        res = []
        backtrack(target, [], 0)
        return res
        
    