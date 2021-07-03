class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        res, running, locations = 0, 0, {0:-1}
        for i, num in enumerate(nums):
            running += num
            if running - k in locations:
                if i - locations[running - k] > res: res = i - locations[running - k]
            if running not in locations: locations[running] = i
        return res