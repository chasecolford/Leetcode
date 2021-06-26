"""
Given an array of integers and an integer k, 
find out whether there are two distinct indices 
i and j in the array such that nums[i] = nums[j] 
and the absolute difference between i and j is at most k.
"""
def containsDuplicate(nums, k):
    d = {}
    for i, v in enumerate(nums):
        if v in d and i - d[v] <= k:
            return True
        d[v] = i
    return False

print(containsDuplicate([1,2,3,1], 3))
print(containsDuplicate([1,0,1,1], 1))
print(containsDuplicate([1,2,3,1,2,3], 2))