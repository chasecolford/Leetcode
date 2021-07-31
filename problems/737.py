class Solution:
    def areSentencesSimilarTwo(self, s1: List[str], s2: List[str], sp: List[List[str]]) -> bool:
        parent = {}
        
        def find(p):
            if p not in parent: parent[p] = p
            while p != parent[p]: p = parent[p]
            return p    
        
        def union(p, q):
            i, j = find(p), find(q)
            if i != j: parent[i] = j
                
        for p, q in sp: union(p, q)
            
        return all(find(a) == find(b) for a, b in zip_longest(s1, s2))

# class Solution:
#     def areSentencesSimilarTwo(self, a, b, s):
#         z = {x:x for x in [s[i][j] for i in range(len(s)) for j in range(2)]+a+b}
#         def f(p): return p if p == z[p] else f(z[p])  
#         def u(p, q): z[i] = j if (i:=f(p)) != (j:=f(q)) else z[i]
#         for p, q in s: u(p, q)
#         return False if len(a)!=len(b) else all(f(p)==f(q) for p,q in zip(a,b)) 