class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # if the bits in (a or b) are currently 1 and they need
        # to be 0 for this position in c, then we need to flip
        # 2 bits to fix this index. If the bits in (a or b) are
        # 0 and they need to be 1, then we need to flip 1 bit
        diff, res = (a | b) ^ c, 0
        for i in range(31):
            mask = 1 << i
            if diff & mask > 0:
                res += 2 if (a & mask) == (b & mask) and (c & mask) == 0 else 1
        return res