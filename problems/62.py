class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        """
        start in the bottom right and use 2d dp to track
        each position. We will move up and left each time,
        where the value at each step is the path count
        from the right + the path count from the bottom
        that lead to a given coordinate (x,y). Once we
        reach the starting square at (0, 0) we are done.
        """
        dp = [[0] * cols for _ in range(rows)]
        dp[rows-1][cols-1] = 1
        for row in range(rows-1,-1,-1):
            for col in range(cols-1,-1,-1):
                if col + 1 < cols: 
                    dp[row][col] += dp[row][col+1]
                if row + 1 < rows:
                    dp[row][col] += dp[row+1][col]
        return dp[0][0]