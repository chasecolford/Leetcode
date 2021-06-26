"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""
"""
#NOTE: Follow up: Could you solve it in-place with O(1) extra space?
"""
# the obvious pythonic way that doesn't address the follow-up:
def reverseWords(s):
    return ' '.join(s.split()[::-1])

#expected "world hello"
print(reverseWords("  hello world  "))