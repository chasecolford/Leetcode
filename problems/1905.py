class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(x, y):
            if not (0 <= x < len(grid2) and 0 <= y < len(grid2[0]) and grid2[x][y] == 1): return 1
            grid2[x][y] = 0
            res = grid1[x][y]
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                res &= dfs(x + dx, y + dy)
            return res
        return sum(dfs(x, y) for x in range(len(grid2)) for y in range(len(grid2[0])) if grid2[x][y])