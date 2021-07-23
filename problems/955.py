class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        res, n, m, ok = 0, len(s), len(s[0]), [0]*(len(s)-1)
        for j in range(m):
            ok2 = ok[:]
            for i in range(n-1):
                if s[i][j] > s[i+1][j] and ok[i] == 0: res += 1; break
                ok2[i] |= s[i][j] < s[i+1][j]
            else: ok = ok2
        return res         