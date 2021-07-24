class Solution:
    def numWays(self, s: str) -> int:
        n, ones, MOD = len(s), [], 10**9+7
        for i, c in enumerate(s):
            if c == '1': ones.append(i)
        count, third = len(ones), len(ones) // 3
        if count == 0: return ((n-1)*(n-2)//2) % (10**9+7) # raw combinations of choosing 2 cuts
        if count % 3 != 0: return 0
        return (ones[third]-ones[third-1]) * (ones[third*2]-ones[third*2-1]) % MOD