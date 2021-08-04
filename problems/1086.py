class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        s = defaultdict(list)
        for i, scr in items: s[i].append(scr)
        return sorted([[i, sum(sorted(s[i])[-5:]) // 5] for i, scr in s.items()])