class Solution:
    def canBeTypedWords(self, text: str, broken: str) -> int:
        bad = set(x for x in broken)
        res = 0
        text = "".join(text).split()
        # print(text)
        for word in text:
            # print(word)
            good = True
            for char in word:
                if char in bad: 
                    good = False
                    break
            if good: res += 1
        return res