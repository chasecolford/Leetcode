class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        count = 1
        last = s[0]
        res = last
        i = 1
        while i < n:
            if count == 2 and s[i] == last: 
                i+=1
                continue
            elif count < 2 and s[i] == last: 
                res += s[i]
                count += 1
            elif s[i] != last:
                last = s[i]
                res += s[i]
                count = 1
            i += 1
        return res
            