class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        alphas = [x for x in S if x.isalpha()]
        print(alphas)
        res = []
        for c in S:
            if c.isalpha():
                res.append(alphas.pop())
            else:
                res.append(c)
        return ''.join(res)