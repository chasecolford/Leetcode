class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter1 = [0] * 26
        counter2 = [0] * 26
        # ascii a = 97
        for i in s:
            counter1[ord(i)-97] += 1
        for j in t:
            counter2[ord(j)-97] += 1
        return True if counter1 == counter2 else False