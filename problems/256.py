class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        push dp:
        if we are at some point i and picking the blue house, for example, we would
        increment the cost of this "path" based on the min of the previous location
        for the other two colors. If we are picking a blue house, this means we had to
        come from a red or green one, so the cost for doing this is tied to what it 
        would cost to have been at a red or green one previously, and so on.
        """
        for i in range(1, len(costs)):
            for j in range(3):
                if j == 0: costs[i][j] += min(costs[i-1][1], costs[i-1][2])
                elif j == 1: costs[i][j] += min(costs[i-1][0], costs[i-1][2])
                elif j == 2: costs[i][j] += min(costs[i-1][0], costs[i-1][1])
        return min(costs[-1])