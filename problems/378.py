class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        from itertools import chain
        return sorted(chain(*matrix))[k-1]