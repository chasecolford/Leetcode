class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        since we can only have two distict characters in out substring, 
        we can use sliding window and always keep track of the widest windows
        we have seen up to some point i
        """
        l, r, counts = 0, 0, {}
        while r < len(s):
            
            # can obv use defaultdict here, decided to do it without imports
            if s[r] not in counts: counts[s[r]] = 1
            else: counts[s[r]] += 1
            
            if len(counts) > 2:
                counts[s[l]] -= 1
                if counts[s[l]] == 0: counts.pop(s[l])
                l += 1
            r += 1
        return r - l