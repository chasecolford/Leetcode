
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # dp represents dp[row][col][up, right, down, left] for row in rows for col in cols
        dp = [[[0] * 4 for _ in range(cols)] for _ in range(rows)]
        
        # load the dp for up, left
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0: dp[row][col][0], dp[row][col][3] = 0, 0
                else: 
                    dp[row][col][0] = 1 if row-1 < 0 else dp[row-1][col][0]+1 # up
                    dp[row][col][3] = 1 if col-1 < 0 else dp[row][col-1][3]+1 # left
                
        # load the dp for down, right
        for row in range(rows-1,-1,-1):
            for col in range(cols-1,-1,-1):
                if grid[row][col] == 0: dp[row][col][1], dp[row][col][2] = 0, 0
                else: 
                    dp[row][col][2] = 1 if row+1 >= rows else dp[row+1][col][2]+1 # down
                    dp[row][col][1] = 1 if col+1 >= cols else dp[row][col+1][1]+1 # right
                    
        res = 0
        
        # iterate the grid: for each grid[i][j], use the dp to find the 
        # largest square the has grid[i][j] as a bottom right corner
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0: continue
                else:
                    p = min(dp[row][col][0], dp[row][col][3]) # min of up, left from this grid[row][col]
                    
                    # check the possible top left starting locaitons for the square 
                    # i.e., move along the main anti-diagonal of the square ending here
                    for i in range(p-1,-1,-1):
                        
                        # check if both the right and down 1s from this top left
                        # square are long enough to form this square ending at grid[row][col]
                        if dp[row-i][col-i][1] > i and dp[row-i][col-i][2] > i: res = max(res, (i+1)*(i+1)); break
        return res