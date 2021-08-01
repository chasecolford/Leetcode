class Solution:
    def numberOfWeeks(self, mile: List[int]) -> int:
        mile.sort()
        s = sum(mile)
        return min((s-mile[-1])*2+1, s)
