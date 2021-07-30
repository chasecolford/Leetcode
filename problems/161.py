class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        a, b = len(s), len(t)
        if s == t or abs(a-b) > 1: return False
        if a < b: s, t, a, b = t, s, b, a # make sure that s is longer, if applicable
        if a == b: return sum((1 if s[i] != t[i] else 0 for i in range(a))) == 1
        else: return any((1 if s[:i] + s[i+1:] == t else 0 for i in range(a))) or any((1 if t[:i] + t[i+1:] == s else 0 for i in range(a)))