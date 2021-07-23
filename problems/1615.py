from collections import defaultdict as dd
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        connected = dd(set)
        for a, b in roads:
            connected[a].add(b)
            connected[b].add(a)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, len(connected[i]) + len(connected[j]) - (i in connected[j]))
        return res