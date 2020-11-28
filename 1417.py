class Solution:
    def reformat(self, s):
        a, b = [], []
        # build the two sets
        for c in s:
            if c.isalpha():
                a.append(c)
            else:
                b.append(c)
        
        # if this case hits, we cant possibly alternate
        if abs(len(a) - len(b)) > 1: return ""
        
        # make sure a is always longest, can also do this with flag
        if len(a) < len(b):
            a, b = b, a
        
        res = []
        for i in range(len(a) + (len(b))):
            if i % 2 == 0:
                res.append(a.pop())
            else:
                res.append(b.pop())
        return res