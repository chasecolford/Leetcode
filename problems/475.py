class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # def bl(h):
        #     l, r = 0, len(heaters) - 1
        #     while l <= r:
        #         m = l+(r-l)//2
        #         if heaters[m] < h: l = m + 1
        #         else: r = m - 1
        #     return l
        heaters.sort()
        r = 0
        for h in houses:
            ind = bisect_left(heaters, h) # way faster, thanks C
            # ind = bl(h)
            if ind == len(heaters): r = max(r, h - heaters[-1])
            elif ind == 0: r = max(r, heaters[0] - h)
            else: r = max(r, min(heaters[ind] - h, h - heaters[ind - 1]))
        return r