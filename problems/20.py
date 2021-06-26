"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true

"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            flag = True
            
        paraCount = 0
        bracketCount = 0
        curlyCount = 0
        lastOpen = []
        flag = True
        
        for char in s:
            #counting logic
            if char == "(": paraCount +=1
            elif char == ")": paraCount -=1
            elif char == "{": curlyCount +=1
            elif char == "}": curlyCount -=1
            elif char == "[": bracketCount +=1
            elif char == "]": bracketCount -=1

            #if we ever close a char we didnt open, return false
            if (paraCount or curlyCount or bracketCount) < 0:
                flag = False
                break

            #last open char logic
            if (char == "(") or (char == "{") or char == ("["):
                lastOpen.insert(0, char)
            elif char == ")":
                if lastOpen == []: 
                    break
                elif lastOpen[0] == "(":
                    lastOpen.pop(0)
                    continue
                else: 
                    flag = False
                    break
            elif char == "}":
                if lastOpen == []: 
                    break
                elif lastOpen[0] == "{":
                    lastOpen.pop(0)
                    continue
                else: 
                    flag = False
                    break
            elif char == "]":
                if lastOpen == []: 
                    break
                elif lastOpen[0] == "[":
                    lastOpen.pop(0)
                    continue
                else: 
                   flag = False
                   break
                    
        if lastOpen == [] and flag:
            return True
        else:
            return False