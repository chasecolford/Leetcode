class Solution:
    def triangleNumber(self, nums):
        res, nums = 0, sorted(nums)
        for i in range(2, len(nums)):
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += (r - l)
                    r -= 1
                else: l += 1
        return res