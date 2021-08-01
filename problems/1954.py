class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        s = n = 0
        while neededApples > s:
            n += 1
            s += 12*pow(n, 2)
        return n * 8