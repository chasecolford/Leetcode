class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        value = lambda word : int(''.join([str(ord(char) - 97) for char in word]))
        return value(firstWord) + value(secondWord) == value(targetWord)