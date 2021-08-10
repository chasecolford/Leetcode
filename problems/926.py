class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = flips = 0
        for i in range(len(s)):
            if s[i] == '1': ones += 1
            else: flips += 1
            flips = min(ones, flips)
        return flips