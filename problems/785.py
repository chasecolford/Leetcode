class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        https://www.youtube.com/watch?v=3VeQhNF5-rE
        make a q, bfs through all the nodes
        only trick is that it is not always connected,
        so we have to try starting the bfs from
        every vertex/node possible, but can skip most of them
        since most of the time they will be colored
        """
        n = len(graph)
        colors = [-1] * n
        for start in range(n):
            if colors[start] != -1: continue # if this node is already colored
            q = deque()
            q.append((start, 0)) # we will always start by 'coloring' the first vertex 0
            
            #bfs
            while q:
                vertex, color = q.popleft()
                if colors[vertex] == -1: # if we have not colored this node yet
                    colors[vertex] = color
                    for nextVertex in graph[vertex]:
                        q.append((nextVertex, color ^ 1)) # xor so 1 becomes 0 and vice versa
                if colors[vertex] != color: # if we find a vert that is the wrong color
                    return False
                
        # if we didnt return inside the queue, the graph is bipartite
        return True