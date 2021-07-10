class Solution:
    def check(self, nums: List[int]) -> bool:
        good = sorted(nums)
        for rot in range(len(nums)):
            if nums[rot:] + nums[:rot] == good:
                return True
        return False