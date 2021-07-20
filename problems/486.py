class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0: return True # https://youtu.be/Tw1k46ywN6E?t=3954
        dp = list(nums)
        
        for length in range(2, len(nums)+1):
            for i in range(len(nums)-length+1):
                dp[i] =  max(nums[i]-dp[i+1], nums[i+length-1]-dp[i]);
          
        return dp[0] >= 0;
        