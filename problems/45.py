class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, farthest, left, right = 0, 0, 0, 0
        
        while right < len(nums) - 1:
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left, right, jumps = right + 1, farthest, jumps + 1
        return jumps