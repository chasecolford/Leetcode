class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        combs(target)= ∑ (i=0 -> n) : combs(target − nums[i]) if target ≥ nums[i]
        n^2 dp: 
        dp is single dimensional, as we only care about the sum at some point dp[i]
        dp = [0] * (target + 1)
        dp[0] = 1 # since there is 1 way to get the empty sum, and we will need to ref this

        pseduo:
        for i in range(1, target):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        """
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[-1]