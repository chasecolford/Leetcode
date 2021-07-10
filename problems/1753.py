class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        big, med, small = (sorted([a, b, c], reverse=True))
        res = 0
        while big > 0 and med > 0:
            res += 1
            big -= 1
            med -= 1
            big, med, small = (sorted([big, med, small], reverse=True))
        return res