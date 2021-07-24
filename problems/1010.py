class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res, counts = 0, [0] * 60
        for t in time:
            res += counts[-t % 60]
            counts[t % 60] += 1
        return res