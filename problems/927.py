class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        indexes = [i for i in range(len(arr)) if arr[i] == 1]
        leni = len(indexes)
        if leni == 0: return [0, 2]
        if leni % 3 != 0: return [-1, -1]
        
        p1, p2 = indexes[0], indexes[leni//3-1]
        p3, p4 = indexes[leni//3], indexes[2*leni//3-1]
        p5, p6 = indexes[2*leni//3], indexes[-1]
        part1, part2, part3 = arr[p1:p2+1], arr[p3:p4+1], arr[p5:p6+1]
        
        if part1 != part2 or part2 != part3: return [-1, -1]
        
        l1, l2, l3 = p3 - p2 - 1, p5 - p4 - 1, len(arr) - p6 - 1
        if l3 > l2 or l3 > l1: return [-1, -1]
        
        return [p2 + l3, p4 + l3 + 1]