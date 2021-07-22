from collections import defaultdict
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(set)
        visited = defaultdict(int)
        for x,y in edges:
            g[x].add(y)
                
        def dfs(node):
            if visited[node] == 1:
                return True
            elif visited[node] == -1:
                return False
            elif len(g[node]) == 0:
                return node==destination
            else:
                visited[node] = -1
                for child in g[node]:
                    if not dfs(child):
                        return False
                visited[node] = 1
                return True
        
        return dfs(source)