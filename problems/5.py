class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # 2D dp that acts as a truth table representing if dp[i][j] in s is palindromic.
        # i.e., if dp[5][7] == 1, this means that s[5:7] is palindromic (actaully s[5 : 7 + 1] since upper bound is exclusve).
        dp = [[0] * len(s) for _ in range(len(s))]
        
        # These hold the indices for the start (left) and end (right) of the best (longest) palindrome found in s.
        # We use these since slicing is not O(1) in python, so we should ideally only slice at the end, not when new longest is found
        left, right = (0, 0) 
        
        # Our first loop iterates in reverse
        for i in range(len(s)-1, -1, -1):
            
            # Our second loop iterates from i to the end of the string
            for j in range(i,  len(s)):
                
                # If the characters in s at position i and j are the same AND
                # if there are one of fewer characters between them OR 
                # if the dp[i + 1][j - 1] is already known to be palindromic
                if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                    
                    # Update the dp for this slice to true, meaning that s[i : j + 1] is palindromic
                    dp[i][j] = 1
                    
                    # If base case OR if our current palindrome is longer than our current longest
                    if (left, right) == (0, 0) or j - i + 1 > (right - left):
                        left, right = i, j
        
        # We use right + 1 since the slice upper bound is exclusive
        return s[left : right + 1]