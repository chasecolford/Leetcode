class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        s, vowels = S.split(), {"a", "e", "i", "o", "u"}
        for i, char in enumerate(s):
            s[i] = char[1:] + char[0] + "ma" + "a" * (i + 1) if char[0].lower() not in vowels else char + "ma" + "a" * (i + 1)  
        return " ".join(s)