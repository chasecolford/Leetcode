"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', 
each representing moving one unit north, south, east, or west, respectively. 
You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
Return True if the path crosses itself at any point, that is, if at any time you are on a location you've previously visited. 
Return False otherwise.
"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        points = {(x, y)}
        for c in path:
            if c == 'N':
                y += 1
            elif c == 'S':
                y -= 1
            elif c == 'E':
                x += 1
            elif c == 'W':
                x -= 1
            if (x,y) in points:
                return True
            else:
                points.add((x, y))
        return False