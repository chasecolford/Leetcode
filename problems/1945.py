class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def toint(x):
            temp = ""
            for char in x:
                temp += str(ord(char) - 96) # 1 index
            return temp
        
        def sumdig(x):
            temp = 0
            for char in str(x):
                temp += int(char)
            return temp
        
        res = 0
        val = toint(s)
        for i in range(k):
            val = sumdig(val)
        return val
            