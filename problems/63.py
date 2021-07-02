class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        """
        very similar to unique paths I, where the only
        difference is that now if a we are at (row, col)
        in our loops, if the position below us in the
        obstacle grid is a 1, we simply dont count paths
        from below it, since they dont exist. The same
        logic applies to if there is an obstacle to the
        right of our current dp location.
        """
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        if grid[rows-1][cols-1] == 1: return 0
        dp[rows-1][cols-1] = 1
        for row in range(rows-1,-1,-1):
            for col in range(cols-1,-1,-1):
                if col + 1 < cols and grid[row][col] == 0:
                    dp[row][col] += dp[row][col+1]
                if row + 1 < rows and grid[row][col] == 0:
                    dp[row][col] += dp[row+1][col]
        return dp[0][0]