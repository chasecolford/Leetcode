class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        # insanely clean solution from lee215
        A = deque(sorted(A))
        for b, i in sorted([-b, i] for i, b in enumerate(B)): B[i] = A.pop() if -b < A[-1] else A.popleft()
        return B