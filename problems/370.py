class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * (length + 1)
        for update in updates:
            res[update[0]] += update[2]
            res[update[1]+1] -= update[2]
        s = 0
        for i in range(length):
            s += res[i]
            res[i] = s
        res.pop()
        return res