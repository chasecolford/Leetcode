class Solution:
    def canPlaceFlowers(self, bed: List[int], n: int) -> bool:
        res, bed = 0, [0] + bed + [0]
        for i in range(1, len(bed) - 1):
            if bed[i-1] == bed[i] == bed[i+1]:
                bed[i] = 1
                res += 1
        return res >= n
        