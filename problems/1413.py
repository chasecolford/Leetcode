"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.
"""
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pref = 0
        minny = 1
        for num in nums:
            pref += num
            minny = max(minny, 1 - pref)
        return minny
    
    