class Solution:
    def confusingNumber(self, n: int) -> bool:
        stringy, rev = str(n), ""
        rotation = {"0" : "0", "1" : "1", "6" : "9", "8" : "8", "9" : "6"}
        for c in stringy[::-1]:
            if c not in rotation: return False
            rev += rotation[c]
        return rev != stringy