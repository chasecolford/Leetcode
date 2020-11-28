# class Solution(object):
#     def removeDuplicates(self, S):
#         res = []
#         for c in S:
#             if res and res[-1] == c:
#                 res.pop()
#             else:
#                 res.append(c)
#         return "".join(res)
import re

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        pair_pattern = r"(.)\1"
        while re.search(pair_pattern, S):
            S = re.sub(pair_pattern, "", S)
        return S