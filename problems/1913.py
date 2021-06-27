class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        return (nums.pop(nums.index(max(nums))) * nums.pop(nums.index(max(nums))) - (nums.pop(nums.index(min(nums))) * nums.pop(nums.index(min(nums)))))