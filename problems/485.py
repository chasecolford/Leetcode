class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current, longest = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                longest = max(current, longest)
            else:
                current = 0
        return longest