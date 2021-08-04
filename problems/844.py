class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a, b = [], []
        for char in s:
            if char == '#' and a: a.pop()
            elif char != '#': a.append(char)
        for char in t: 
            if char == '#' and b: b.pop()
            elif char != '#': b.append(char)
        return a == b