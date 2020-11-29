class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = []
        for p in points:
            xs.append(p[0])
        xs.sort()
        large = 0
        for i in range(len(xs)-1):
            d = xs[i+1] - xs[i]
            if d > large: large = d
        return large