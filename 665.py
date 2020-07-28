"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

 

Constraints:

    1 <= n <= 10 ^ 4
    - 10 ^ 5 <= nums[i] <= 10 ^ 5

"""
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [float("-inf")] + nums + [float("inf")]
        count = 0
        
        for i in range(1, len(nums)-1):
            
            if nums[i] > nums[i+1]:
                index = i
                count += 1
                if count == 2:
                    return False
                
        if count == 0: return True
        
        if count == 1 and nums[index-1]<= nums[index+1]: return True
        
        if count == 1 and nums[index] <= nums[index+2]: return True
                            
        return False