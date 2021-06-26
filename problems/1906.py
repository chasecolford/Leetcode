class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        L = len(nums)
        counts = [[0] * 101 for _ in range(L + 1)]
        
        for i in range(L):
            for j in range(101):
                counts[i + 1][j] = counts[i][j]
            counts[i + 1][nums[i]] += 1
        
        res = []
        for start, end in queries:
            best = 10**5
            last = -10**6
            for k in range(1, 101):
                if counts[end + 1][k] - counts[start][k] > 0:
                    best = min(best, k - last)
                    last = k
            if best == 10**5:
                res.append(-1)
            else:
                res.append(best)
                
        return res