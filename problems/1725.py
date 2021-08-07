class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res = maxl = 0
        for r in rectangles: res, maxl = (1, min(r)) if min(r) > maxl else (res+1, maxl) if min(r) == maxl else (res, maxl)
        return res