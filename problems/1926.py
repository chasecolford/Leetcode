import collections
class Solution:
    def nearestExit(self, maze: List[List[str]], start: List[int]) -> int:
        
        """
        start at the start location, bfs, return the first time we find 
        a valid exit
        """
        # generate the possible exit locations
        
        # we are given the entrance
        rows, cols = len(maze), len(maze[0])
        directions = [(0, -1), (0, 1), (1, 0), (-1,0)]
        seen = set()
        
        print(start)
        sx, sy = start
        deque = collections.deque([(sx, sy)])
        res = 0
        
        while deque:
            size = len(deque)
            
            for i in range(size):
                r, c = deque.popleft()
                seen.add((r, c))
                
                # if this is an empty cell
                if maze[r][c] == ".":
                    
                    # determine if we are on the edge
                    if r == 0 or c == 0 or r == rows-1 or c == cols-1:
                        
                        # make sure this isnt exit
                        if [r, c] != start:
                            return res
            
                # now for each of the valid direction
                for dx, dy in directions:
                    x = r + dx
                    y = c + dy

                    if 0 <= x < rows and 0 <= y < cols and maze[x][y] != "+" and (x,y) not in seen:
                        deque.append((x,y))
                        seen.add((x,y))
            
            res += 1
    
        return -1