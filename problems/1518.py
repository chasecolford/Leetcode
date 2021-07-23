class Solution:
    def numWaterBottles(self, bottles: int, exchange: int) -> int:
        # or, if my brain was bigger :)
        return bottles + (bottles - 1)//(exchange - 1)
    
        # res = 0
        # full = bottles
        # empty = 0
        # while full > 0:
        #     res += full
        #     newfull, newempty = divmod(full + empty, exchange)
        #     empty = newempty
        #     full = newfull
        # return res