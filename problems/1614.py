class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or ("(" not in s):
            return 0
        
        depth = 0
        answer = 0
        
        for i in s:
            if i == "(":
                depth += 1
            if i == ")":
                depth -= 1
            if depth > answer:
                answer = depth
        return answer