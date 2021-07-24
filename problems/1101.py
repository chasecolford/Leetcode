class Solution:
     def earliestAcq(self, logs, n):
        uf = {x:x for x in range(n)}
        self.components = n
        
        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                self.components -= 1
                uf[x] = y
        
        def find(x):
            if uf[x] != x: uf[x] = find(uf[x])
            return uf[x]
        
        for t, x, y in sorted(logs):
            union(x, y)
            if self.components == 1: return t
        
        return -1