"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
def twoSum(nums, target):
    compliments = {}
    for i, num in enumerate(nums):
        if num in compliments:
            return [compliments[num], i]
        else:
            compliments[target - num] = i

#expected 9
print(twoSum([2,7,11,15], 9))