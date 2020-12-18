class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj, cnt = nums[0], 1
        for i in range(1, len(nums)):
            if cnt == 0:
                cnt += 1
                maj = nums[i]
            elif maj == nums[i]: cnt += 1
            else: cnt -= 1
        return maj

# see: http://www.cs.utexas.edu/~moore/best-ideas/mjrty/