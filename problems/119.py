class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pt = [[1]]
        for i in range(1, rowIndex+1):
            pt.append([1])
            for j in range(i-1):
                pt[i].append(pt[i-1][j] + pt[i-1][j+1])
            pt[i].append(1)
        return pt[rowIndex]