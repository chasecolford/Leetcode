class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        return (set(j[1] for j in paths) - set(i[0] for i in paths)).pop()