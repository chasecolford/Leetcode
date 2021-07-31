from collections import defaultdict as dd, deque as Q
class Solution:
    def checkIfPrerequisite(self, c: int, preq: List[List[int]], qs: List[List[int]]) -> List[bool]:
        
        # build graph
        g = dd(list, {i:[] for i in range(c)})
        for a, b in preq: g[a] += [b]
        
        # store if a:=q[0], b:=q[1] dp[a][b] is reachable, meaing a isPreReq b
        dp = [[False] * 100 for _ in range(c)]
        
        # bfs from every course and assign dp[bfsStart][visitedNode] to be reachable
        for i in range(c):
            q, seen = Q([i]), set()
            while q:
                cur = q.pop()
                seen.add(cur)
                for course in g[cur]:
                    if course in seen: continue
                    dp[i][course] = True
                    q.append(course)
                    seen.add(course)
        
        return [dp[i][j] for i, j in qs]
            