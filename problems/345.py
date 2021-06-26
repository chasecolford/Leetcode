"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"

Example 2:

Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ans = list(s)
        chars = []
        indexes = []

        for i in range(len(s)):
            if s[i] in vowels:
                chars.append(s[i])
                indexes.append(i)

        chars = chars[::-1]

        for x in range(len(chars)):
            ans[indexes[x]] = chars[x]
        
        return "".join(ans)