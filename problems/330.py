class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss, added, i, l = 1, 0, 0, len(nums)
        while miss <= n:
            if i < l and nums[i] <= miss: miss, i = miss + nums[i], i + 1
            else: miss, added = miss + miss, added + 1
        return added