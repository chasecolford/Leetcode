class Solution:
    def matrixReshape(self, mat: List[List[int]], newrow: int, newcol: int) -> List[List[int]]:
        
        row, col = len(mat), len(mat[0])
        
        # If the reshape operation with given parameters is possible and legal, 
        # output the new reshaped matrix; Otherwise, output the original matrix.
        if row * col != newrow * newcol: return mat
        
        """ dont really need to use this, but good to know i guess
        2d -> 1d: M[i][j]=M[n*i+j]
        1d -> 2d: M[i] => M[i/n][n%i]
        """
        # flat = [val for row in mat for val in row]

        res = [[0] * newcol for _ in range(newrow)]
        for i in range(newrow * newcol):
            res[i // newcol][i % newcol] = mat[i // col][i % col]
        return res
        