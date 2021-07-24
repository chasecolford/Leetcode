class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # lee strikes again
        res = need = 0
        for i in sorted(nums):
            res += max(need - i, 0)
            need = max(need + 1, i + 1)
        return res