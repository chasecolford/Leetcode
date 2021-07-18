class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        """
        greedy add them as far away as we can until we can reach the next one.
        """
        pos, res = 0, 0
        for rung in rungs:
            curdist = abs(rung - pos)
            print(pos, rung, curdist)
            if curdist > dist:
                res += ceil(curdist / dist) - 1
            pos = rung
        return res
        