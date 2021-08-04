class Solution:
    def relativeSortArray(self, A: List[int], B: List[int]) -> List[int]:
        k = {b: i for i, b in enumerate(B)}
        return sorted(A, key=lambda a: k.get(a, 1000 + a))