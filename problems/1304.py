class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        cur = 1
        if n % 2 == 0:
            for i in range(n // 2):
                res.append(cur)
                res.append(-cur)
                cur += 1
        else:
            res.append(0)
            for i in range(n // 2):
                res.append(cur)
                res.append(-cur)
                cur += 1
        return res
    
        #return range(1 - n, n, 2)