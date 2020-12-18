"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
def maxSubarray(nums):
    dp = [nums[0]]
    for i in range(1, len(nums)):
        dp.append(max(nums[i], dp[i-1] + nums[i]))
    return max(dp)

# alternative from @_LeetCode
# def maxSubarray(nums):
#     for i in range(1, len(nums)):
#         if nums[i-1] > 0:
#             nums[i] += nums[i-1]
#     return max(nums)


#expected 6
print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))
