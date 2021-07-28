class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res, stack = [0]*len(heights), []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] < height: res[stack.pop()] += 1
            if stack: res[stack[-1]] += 1 # the last taller person can see our current person too
            stack.append(i)
        return res