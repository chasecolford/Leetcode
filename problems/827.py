class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        1. find all the islands (dfs from all 1 locations, track seen)
            a. color each island a unique color
            b. store the size of each island w/ the color
        2. check up, down, left, right from each zero (just 1 unit in each direction)
            and calculate the total size of all islands it touches/connects + 1 (itself)
            we will use the fact that each island has a unique color to ensure that we dont
            count the same color island twice, since a single 0 may touch the same island 
            more than 1 time.
        """
        n, seen, color, colorsize = len(grid), {}, 0, {}
        
        dirs = [(1,0), (0,1), (-1,0), (0,-1)] #URDL
        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= n: return
            if grid[r][c] == 0 or (r, c) in seen: return 
            seen[(r, c)] = color
            if color not in colorsize: colorsize[color] = 0
            colorsize[color] += 1
            for d in dirs: dfs(r+d[0], c+d[1])
                
        # find all of the islands / 'components'
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in seen:
                    # seen[(r, c)] = color
                    dfs(r, c)
                    color += 1
        
        res = max(size for size in colorsize.values()) if len(colorsize) > 0 else 0
        for r in range(n):
            for c in range(n):
                islandsize = 0
                if grid[r][c] == 0:
                    colors = set() # make sure we dont count the same colors more than once
                    for d in dirs:
                        y, x = r+d[0], c+d[1]
                        if y < 0 or x < 0 or y >= n or x >= n: continue
                        if grid[y][x] == 1:
                            if seen[(y, x)] in colors: continue
                            islandsize += colorsize[seen[(y, x)]]
                            colors.add(seen[(y, x)])
                res = max(res, islandsize + 1)
        return res
                      