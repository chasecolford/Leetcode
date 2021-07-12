class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # a, b = [0]*256, [0]*256
        # for i in range(len(s)):
        #     if a[ord(s[i])] != b[ord(t[i])]:
        #         return False
        #     a[ord(s[i])] = i + 1
        #     b[ord(t[i])] = i + 1
        # return True
    
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))