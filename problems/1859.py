class Solution:
    def sortSentence(self, sentence: str) -> str:
        words = [""] * 10
        for word in sentence.split():
            words[int(word[-1])] = word[:-1]
        return ' '.join(words).strip()