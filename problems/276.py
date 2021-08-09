class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0: return 0
        elif n == 1: return k
        elif n == 2: return k * k
        
        dp = [0, k, k*k] + [0]*(n-2)
        for i in range(3, n+1): dp[i] = (dp[i-1]+dp[i-2]) * (k-1)
        return dp[n]
