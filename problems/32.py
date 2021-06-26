"""
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.
"""
def longestValidParentheses(s):
    stacky, maxxy = [(')', -1)], 0
    for i in range(len(s)):
        if s[i] == ')' and stacky[-1][0] == '(':
            stacky.pop()
            maxxy = max(i - stacky[-1][1], maxxy)
        else:
            stacky.append((s[i], i))
    return maxxy

# expected: 2
print(longestValidParentheses("(()"))

# expected: 4
print(longestValidParentheses(")()())"))