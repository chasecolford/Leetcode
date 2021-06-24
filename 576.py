class Solution:
    def findPaths(self, rows: int, cols: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[([0] * cols) for _ in range(rows)] for _ in range(maxMove + 1)]
        outside = 0
        
        dp[0][startRow][startColumn] = 1 # init the starting position
        
        for move in range(maxMove):
            for r in range(rows):
                for c in range(cols):
                    
                    # this represents the number of ways to get to this position using
                    # exactly the current amount of moves
                    current = dp[move][r][c]
                    
                    # ensuring we dont waste time on empty cells -> good speed increase for a simple check
                    if current > 0:
                        
                        # for each of the four directions
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc

                            # if we are not outside yet. add these values to dp
                            if 0 <= nr < rows and 0 <= nc < cols:
                                dp[move + 1][nr][nc] += current
                                dp[move + 1][nr][nc] %= MOD

                            # else, we are outside, add this to out total outside
                            else:
                                outside += current
                                outside %= MOD
                            
        return outside % MOD