class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        l, r = 0, len(nums) - 1
        while l < len(nums) - 1 and nums[l] <= nums[l + 1]: l += 1 # first decreasing
        while r > 0 and nums[r] >= nums[r -1]: r -= 1 # first increasing
        if l > r: return 0 # array is already sorted
        temp = nums[l:r+1]
        mn, mx = min(temp), max(temp)
        while l > 0 and mn < nums[l-1]: l -= 1 # find vals left of l that are > mn
        while r < len(nums) - 1 and mx > nums[r+1]: r += 1 # find vals right of r that are < mx
        return r - l + 1