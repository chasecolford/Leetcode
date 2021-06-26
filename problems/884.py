import collections
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        c = collections.Counter((A + " " + B).split())
        return [x for x in c if c[x] == 1]