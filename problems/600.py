class Solution:
    def findIntegers(self, n: int) -> int:
        # the 30 fibs we could need (30 because the max num is 10**9 which has 30 bits)
        fibs = [1, 2, 3, 5, 8, 13, 21, 34,
                55, 89, 144, 233, 377, 610, 987, 1597, 
                2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 
                121393, 196418, 317811, 514229, 832040, 1346269]
        
        res, flag = 0, 0
        for i in range(29,-1,-1):
            if (1 << i) & n: # if the ith bit is 1
                res += fibs[i]
                if flag: return res # two 1s found, return
                flag = 1
            else: flag = 0
        return res + 1