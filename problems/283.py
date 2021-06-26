class Solution(object):
    def moveZeroes(self, nums):
        nonzero = 0  # last index of non-zero / start of where we want 0 to be placed
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[nonzero] = nums[nonzero], nums[i]
                nonzero += 1