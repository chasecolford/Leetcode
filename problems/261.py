class Solution:
    def validTree(self, n, edges):
        parent = list(range(n))
        def find(x): return x if parent[x] == x else find(parent[x])
        def union(xy):
            x, y = map(find, xy)
            parent[x] = y
            return x != y
        return len(edges) == n-1 and all(map(union, edges))