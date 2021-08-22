class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        for i in range(1, n):
            m1 = min(costs[i-1])
            index = costs[i-1].index(m1)
            m2 = min(costs[i-1][:index] + costs[i-1][index+1:])
            for j in range(k): costs[i][j] = costs[i][j] + m2 if j == index else costs[i][j] + m1
        return min(costs[-1])