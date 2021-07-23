from collections import defaultdict as dd
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0    
        roads = set()
        graph = collections.defaultdict(list)
        for u, v in connections:
            roads.add((u, v))
            graph[v].append(u)
            graph[u].append(v)
        def dfs(u, parent):
            self.res += (parent, u) in roads
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)    
        dfs(0, -1)
        return self.res
    
#         graph, ugraph, seen = dd(set), dd(set), set()
#         for x,y in connections: 
#             graph[x].add(y)
#             ugraph[x].add(y)
#             ugraph[y].add(x)
        
#         self.res = 0
#         def dfs(node, parent):
#             if node in seen: return
#             seen.add(node)
            
#             if parent in graph and node in graph[parent]: self.res += 1
            
#             for edge in ugraph[node]:
#                 dfs(edge, node)
                
#         dfs(0, None)
#         return self.res
        