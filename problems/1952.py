class Solution:
    def isThree(self, n: int) -> bool:
        temp = 0
        for i in range(1, n+1):
            if n % i == 0: temp += 1
        return (temp == 3)