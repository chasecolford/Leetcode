class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = count = res = s = 0
        for r, i in enumerate(nums):
            s += i
            if i == 1: count = 0
            while l <= r and s >= goal:
                if s == goal: count += 1
                s, l = s-nums[l], l+1
            res += count
        return res
            