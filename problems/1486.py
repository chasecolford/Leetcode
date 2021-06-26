class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        # x = start
        # for i in range(start+2, start+(n*2), 2):
        #     x^=i
        # return x
            
        x = 0
        for i in range(0, n):
            x ^= start + 2 * i
        return x
        # var xorOperation = function(n, start) {
        # let xor = 0
        # for (let i=0; i<n ; i++){
        #     xor ^= start + 2 * i
        # }
        # return xor
        # };