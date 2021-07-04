class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        layout = {key: index for index, key in enumerate(keyboard)}
        time, pos = 0, 0
        for c in word:
            nextpos = layout[c]
            time += abs(pos - nextpos)
            pos = nextpos
        return time