class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        for i in range(n-2):
            t = t0+t1+t2
            t0 = t1
            t1 = t2
            t2 = t
        return t2