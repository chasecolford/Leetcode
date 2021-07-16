class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                goal = target - nums[i] - nums[j]
                l, r = j + 1, len(nums) - 1

                while l < r:
                    if nums[l] + nums[r] < goal: l += 1
                    elif nums[l] + nums[r] > goal: r -= 1
                    else:
                        res.append((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1

        return set(res)
