class Solution:
    def minSwaps(self, s: str) -> int:
        stack = 0
        swaps = 0
        
        for c in s:
            if c == "[":
                stack += 1
            else:
                if stack == 0:
                    stack += 1
                    swaps += 1
                else:
                    stack -= 1
        return swaps