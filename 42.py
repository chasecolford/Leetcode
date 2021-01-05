"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        res, s = 0, []
        for i in range(len(height)):
            while len(s) > 0 and (height[i] > height[s[-1]]):
                cur = s.pop()
                if len(s) == 0: break
                dist = i - s[-1] - 1
                bound = min(height[i], height[s[-1]]) - height[cur]
                res += dist * bound      
            s.append(i)
        return res