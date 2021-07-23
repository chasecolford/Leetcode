class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        rights = [0] * n # store min of right partitions (left must be non-empty)
        small = float('inf')
        for i in range(n-1, 0, -1):
            small = min(small, nums[i])
            rights[i] = small
         
        big = -1
        for j in range(n-1):
            big = max(big, nums[j])
            if big <= rights[j+1]: return j+1