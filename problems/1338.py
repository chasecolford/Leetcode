from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        mostcommon, half, removed, res,  = Counter(arr).most_common(), len(arr) // 2, 0, 0
        for val, count in mostcommon:
            res, removed = res + 1, removed + count
            if removed >= half: return res
        return res