class Solution:
    def maxPoints(self, A):
        #lee215 solution
        m, n = len(A), len(A[0])
        for i in range(m - 1):
            for j in range(n - 2, -1, -1):
                A[i][j] = max(A[i][j], A[i][j + 1] - 1)
            for j in range(n):
                A[i][j] = max(A[i][j], A[i][j - 1] - 1 if j else 0)
                A[i + 1][j] += A[i][j]
        return max(A[-1])