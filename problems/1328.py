class Solution:
    def breakPalindrome(self, p: str) -> str:
        if len(p) == 1: return ''
        for i in range(len(p)):
            if p[i] != 'a' and not (i == len(p) // 2 and len(p) % 2):
                return p[:i] + 'a' + p[i+1:]
        return p[:-1] + 'b'