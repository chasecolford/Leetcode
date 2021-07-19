class Solution:
    def numSplits(self, s: str) -> int:
        """
        so this one seems easy, there are only n-1 possible splits,
        since the concatenation must == s. We can simply keep dicts of
        each of the sides and compare lengths to see if good.
        """
        res = 0
        left, right = {s[0]: 1}, {}
        for i in range(1, len(s)):
            if s[i] not in right: right[s[i]] = 1
            else: right[s[i]] += 1
        
        if len(left) == len(right): res += 1
        
        # now that we have the right and left dicts, we can compare each split
        for i in range(1, len(s)):
            
            # add / increment this char in left
            if s[i] not in left: left[s[i]] = 1
            else: left[s[i]] += 1
            
            # subract / decrement this char in right
            if right[s[i]] == 1: right.pop(s[i])
            else: right[s[i]] -= 1
            
            if len(left) == len(right): res += 1
        
        return res