class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s = Counter(s)
        last = -1
        for c, v in s.items():
            if last == -1: last = v; continue
            if last != v: return False
        return True