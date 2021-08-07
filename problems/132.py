class Solution:
    def minCut(self, s):
        if s == s[::-1]: return 0 # if s is already a plaindrome
        n = len(s)
        for i in range(1, n):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]: return 1

        pal, dp = [[0] * (i+1) for i in range(n)], list(range(n)) + [-1]
        for i in range(n):
            for j in range(i,-1,-1):
                if s[i] == s[j] and (i - j < 2 or pal[i-1][j+1]):
                    pal[i][j] = 1
                    dp[i] = min(dp[i], dp[j-1]+1)
                    
        return dp[n-1]
