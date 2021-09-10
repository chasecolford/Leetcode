class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops: return m * n
        X, Y = zip(*ops)
        return min(X) * min(Y)