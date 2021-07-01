class Solution:
    def countBits(self, n: int) -> List[int]:
        res, offset = [0] * (n + 1), 1
        for i in range(1, n + 1):
            if offset * 2 == i: offset *= 2
            res[i] = res[i - offset] + 1
        return res