class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        m, n = len(mat[0]), len(mat)
        r1 = any(mat[0][j] == 0 for j in range(m))
        c1 = any(mat[i][0] == 0 for i in range(n))
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0: mat[i][0] = mat[0][j] = 0  
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] * mat[0][j] == 0: mat[i][j] = 0     
        if r1:
            for i in range(m): mat[0][i] = 0 
        if c1:
            for j in range(n): mat[j][0] = 0