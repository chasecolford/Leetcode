class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        """
        Given a square matrix mat, return the sum of the matrix diagonals.
        n == mat.length == mat[i].length
        1 <= n <= 100
        1 <= mat[i][j] <= 100
        """
        
        #if the matrix is even edge length, diagonals dont overlap
        #if odd edge length, only count middle val once since they overlap
        
        edge = len(mat) #would be vertical edge, mat[0] is horiz; however, since it is square, doesnt matter here
        
        #edge cases
        if edge == 1:
            return mat[0][0]
        if edge == 2:
            return sum(mat[0]) + sum(mat[1])
        
        answer = 0
        
        #primary diagonal
        for i in range(edge):
            answer += mat[i][i]
            
        #secondary diagonal
        for i in range(edge):
            answer += mat[i][(edge - 1) - i]
        
        #check for odd to see if we remove middle elem double count
        if edge % 2 == 1:
            answer -= mat[(edge-1)//2][(edge-1)//2]
        
        return answer