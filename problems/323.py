from collections import defaultdict as dd
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        dfs from every node, while tracking visited.
        each time we start a new dfs and find at least 1
        new node, we have a new section 'component'
        """
        def dfs(vert):
            if vert in seen: return
            seen.add(vert)
            for v in graph[vert]: dfs(v)

        graph, seen = dd(list), set()
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                res += 1
                
        return res