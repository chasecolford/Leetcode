class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res, l, r, same = len(wordsDict), len(wordsDict), -len(wordsDict), word1 == word2     
        for i, word in enumerate(wordsDict):
            if word == word1: l = r if same else i
            if word == word2: r = i
            res = min(res, abs(l - r))
        return res