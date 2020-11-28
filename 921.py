class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        right = 0
        left = 0
        for i in S:
            if right == 0 and i == ')':
                left += 1
            else:
                right += 1 if i == '(' else -1
        return left + right