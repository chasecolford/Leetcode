class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        possible = set([x**2 for x in range(1, n+1)])
        print(possible)
        for i in range(1, n+1):
            for j in range(1, n+1):
                if (i**2) + (j**2) in possible: res += 1        
        return res