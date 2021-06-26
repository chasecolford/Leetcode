class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        for k,v in d.items():
            if v == 1:
                return s.index(k)
        return -1