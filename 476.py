class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num ^ 2 ** num.bit_length() - 1
