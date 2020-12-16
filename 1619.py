"""
Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

Answers within 10-5 of the actual answer will be considered accepted.
"""
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        return sum(sorted(arr)[n//20 : - n//20]) / (n * 9 // 10)