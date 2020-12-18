"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        #literally fib
        if n == 1: return 1
        if n == 2: return 2
        lastlast, last = 1, 2
        for i in range(2, n):
            lastlast, last = last, last + lastlast
        return last
        