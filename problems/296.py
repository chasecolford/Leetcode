class Solution:
    def minTotalDistance(self, grid):
        return sum(sum(abs(x - X[len(X)//2]) for x in X) for X in
               ([x for x, row in enumerate(grid) for _ in range(sum(row))]
                for grid in (grid, zip(*grid))))