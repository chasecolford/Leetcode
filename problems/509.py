class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        
        minus2 = 0
        minus1 = 1
        answer = 1 #this assumes we already did F(1)
        
        for i in range(1, N-1):
            minus2 = minus1
            minus1 = answer
            answer = minus1 + minus2
        return answer