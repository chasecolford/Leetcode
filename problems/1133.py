class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        res = -1
        for k, v in c.items():
            if k > res and v == 1: res = k
        return res