class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        for i, w in enumerate(sentence.split(" ")):
            if w[:len(searchWord)] == searchWord:
                return i + 1
        return -1
        