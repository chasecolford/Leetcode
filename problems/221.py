class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        # https://www.youtube.com/watch?v=oPrpoVdRLtg 
        # errichto video is insanely helpful for visualizing this
        
        rows = len(mat)
        if rows == 0: return 0
        cols = len(mat[0])
        
        res = 0
        dp = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == "1": 
                    dp[r][c] = 1
                    if r > 0 and c > 0: 
                        dp[r][c] += min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
                    res = max(res, dp[r][c])
                
        return res * res