class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        # calculates the distance between two points
        def distance(x1, y1, x2, y2):
            return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** .5
        
        # store the count of points for each query
        # i.e., res[i] == the amount of points within the circle for the ith query
        res = [0] * len(queries)
        
        # for each of our queries
        for i, query in enumerate(queries):
            x, y, r = query
            
            
            # for each of the points
            for point in points:
                if distance(*point, x, y) <= r:
                    res[i] += 1
        
        return res