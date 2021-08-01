class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp, MOD = [1, 0, 0, 0], 10**9 + 7
        for i in nums: dp[i+1] += (dp[i+1] + dp[i]) % MOD
        return dp[-1] % MOD