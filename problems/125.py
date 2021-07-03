class Solution:
    def isPalindrome(self, s: str) -> bool:
        # no thanks
        cleaned = [c.lower() for c in s if c.isalnum()]
        return cleaned==cleaned[::-1]