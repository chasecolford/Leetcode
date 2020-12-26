"""
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original 
string by deleting some (can be none) of the characters without disturbing 
the relative positions of the remaining characters. 
(ie, "ace" is a subsequence of "abcde" while "aec" is not).
"""
def isSubsequence(s, t):
    if s == "": return True
    si = 0 # track the position of the next char we are searching for from s in t
    for c in t:
        if c == s[si]:
            si += 1
        if si == len(s): return True
    return False

#expected true
print(isSubsequence("abc", "ahbgdc"))

#expected false
print(isSubsequence("axc", "ahbgdc"))

#expected false
print(isSubsequence("acb", "ahbgdc"))