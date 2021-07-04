class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 1: return 5
        
        # space optimized since we only ever need the i-1 dp
        dp = [0] * 5
        prevdp = [0] * 5
        
        for x in range(5): prevdp[x] = 1
        
        for i in range(2, n + 1):
            """ RULES:
            Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
            Each vowel 'a' may only be followed by an 'e'.
            Each vowel 'e' may only be followed by an 'a' or an 'i'.
            Each vowel 'i' may not be followed by another 'i'.
            Each vowel 'o' may only be followed by an 'i' or a 'u'.
            Each vowel 'u' may only be followed by an 'a'.
            """
            dp = [0] * 5 # reset the current dp
            dp[0] = (prevdp[1] + prevdp[2] + prevdp[4]) % MOD
            dp[1] = (prevdp[0] + prevdp[2]) % MOD
            dp[2] = (prevdp[1] + prevdp[3]) % MOD
            dp[3] = prevdp[2] % MOD
            dp[4] = (prevdp[2] + prevdp[3]) % MOD
            prevdp = dp # set the previous to equal this new dp
            
        return sum(dp) % MOD