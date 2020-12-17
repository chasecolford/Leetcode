"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        res = [[1], [1,1]]
        for i in range(2, numRows):
            temp = [1]
            for j in range(1, len(res[-1])): # get the last row from triangle
                temp.append(res[i-1][j] + res[i-1][j-1])
            res.append(temp + [1])
        return res

# others @girikuncoro
# def generate(numRows):
#     pascal = [[1]*(i+1) for i in range(numRows)]
#     for i in range(numRows):
#         for j in range(1,i):
#             pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
#     return pascal