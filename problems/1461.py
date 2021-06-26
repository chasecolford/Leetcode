"""
Given a binary string s and an integer k.

Return True if every binary code of length k is a substring of s. Otherwise, return False.
"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        # one line
        # return len({s[i : i + k] for i in range(len(s) - k + 1)}) == 2**k
    
        # verbose
        distinctBinaryStringsSet = set({})
        for i in range(len(s) - k + 1):
            distinctBinaryStringsSet.add(s[i:i+k])
        if len(distinctBinaryStringsSet) == 2 ** k:
            return True
        else:
            return False