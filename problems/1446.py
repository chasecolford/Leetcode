class Solution:
    def maxPower(self, s: str) -> int:
        ptr, cur, res, last = 1, 1, 1, s[0]
        while ptr < len(s):
            if s[ptr] == last: 
                cur += 1
                if cur > res: res = cur
            else: cur = 1
            
            last = s[ptr]
            ptr += 1
        return res