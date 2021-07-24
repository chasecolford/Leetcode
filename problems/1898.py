class Solution:
    def maximumRemovals(self, s: str, p: str, rem: List[int]) -> int:
        
        # returns true if sub is subsequence of string
        def issub(string):
            i = j = 0
            while i < len(s):
                if letters[i] != '?' and s[i] == p[j]: j += 1
                if j == len(p): return True
                i += 1
            return False
                
        # build array for chars for faster changes
        letters = [c for c in s]
        l, r = 0, len(rem)
        while l <= r:
            m = l + (r - l) // 2
            for i in range(m): letters[rem[i]] = '?' # placeholder symbol that represents not there, faster than concat strings
            if issub(letters): l = m + 1
            else: 
                for i in range(m): letters[rem[i]] = s[rem[i]] # fix the letters we changed to placeholders
                r = m - 1
                
        return r # we exit the bin search with r being 1 less than l, which is the last char we could take, so return r