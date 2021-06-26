class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = ''.join(chr(x) for x in range(1001)) # 3 <= n <= 1000
        for a, b in edges:
            if graph[a] == graph[b]: return [a, b]
            graph = graph.replace(graph[a], graph[b])