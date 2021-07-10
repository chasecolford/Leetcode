# sick problem, will need to do more like this before i can quickly code this in contest
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        ######################
        # kruskals algorithm #
        ######################
        
        # union find
        def find(city):
            if parent[city] != city: parent[city] = find(parent[city])
            return parent[city]
        
        def union(city1, city2):
            root1, root2 = find(city1), find(city2)
            if root1 == root2: return False
            parent[root2] = root1
            return True
        
        # core of kruskals
        res = 0
        # [1] initially, all of the cities are in their own set
        parent = {city: city for city in range(1, n+1)}
        
        # [2] we need to sort the connections based on the cost of the edge
        connections.sort(key=lambda x: x[2])
        
        # [3] for each of the connections, if we have valid cities to union, add the path cost
        for city1, city2, cost in connections:
            if union(city1, city2): res += cost
                
        # make sure that all the cities are connected
        root = find(n)
        return res if all(root == find(city) for city in range(1, n+1)) else -1