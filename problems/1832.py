class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        from string import ascii_lowercase as A
        return all(c in sentence for c in A)