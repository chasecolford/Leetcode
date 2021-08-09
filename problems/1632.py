class Solution:
    def matrixRankTransform(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        rank = [0] * (m + n)
        d = collections.defaultdict(list)
        
        def find(i):
            if p[i] != i: p[i] = find(p[i])
            return p[i]
        
        
        for i in range(n):
            for j in range(m):
                d[mat[i][j]].append([i, j])

        for a in sorted(d):
            p, rank2 = list(range(m + n)), rank[:]
            for i, j in d[a]:
                i, j = find(i), find(j + n)
                p[i] = j
                rank2[j] = max(rank2[i], rank2[j])
            for i, j in d[a]: rank[i] = rank[j + n] = mat[i][j] = rank2[find(i)] + 1
                
        return mat