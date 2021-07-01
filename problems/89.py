class Solution:
    def grayCode(self, n: int) -> List[int]:
        # https://cp-algorithms.com/algebra/gray-code.html
        res = []
        for i in range(2**n):
            res.append(i ^ (i >> 1))
        return res