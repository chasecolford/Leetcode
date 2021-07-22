class Solution:
    def maxScoreSightseeingPair(self, vals: List[int]) -> int:
        # like best time to buy and sell stock
        res, mx = 0, vals[0] - 1
        for i in range(1, len(vals)):
            res = max(res, mx + vals[i])
            mx = max(mx, vals[i]) - 1
        return res