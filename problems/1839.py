class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        """
        the string must contain the aeiou in order, so a before e, e before i, etc.
        therefore, greedy
        """
        res, cur, unique = 0, 1, 1
        for i in range(1, len(word)):
            if word[i-1] <= word[i]:
                cur += 1
                if word[i-1] < word[i]: unique += 1
            else: cur = unique = 1
            if unique == 5: res = max(res, cur)
        return res