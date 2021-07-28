class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # apparently bruteforce is accepted..
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s