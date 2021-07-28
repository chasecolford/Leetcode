class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        
        if len(s) != len(t): return False
        if s == t: return True
        
        shifts = {}
        def shift(a, b):
            """Returns the shift amount required to make a into b"""
            if a == b: return 0
            return abs(ord(a) - ord(b)) if a < b else 26 - (ord(a) - ord(b))
        
        for i, char in enumerate(s):
            a = shift(s[i], t[i])
            if a == 0: continue # dont care about chars that are already right
            if a in shifts: shifts[a] += 1
            else: shifts[a] = 1

        for s, c in shifts.items():
            if s > k: return False
            if (c - 1) * 26 + s > k: return False
            
        return True