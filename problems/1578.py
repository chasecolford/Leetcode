class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        """
        no matter what the costs are, we need to make sure we
        dont the same char next to eachother; therefore,
        we can find all the locations where we have this in the input
        string reduce these sections down to just a single character.
        obviously, when doing this, we should leave the most 
        expensive one in the string.
        """
        res = highest = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i - 1]: highest = 0
            res += min(highest, cost[i])
            highest = max(highest, cost[i])
        return res