# contest style submission, not optimized for runtime.
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:        
        return 0 if (k > 26 or k > len(s)) else sum([1 for i in range(len(s)-k+1) if len(set(s[i:i+k])) == k])