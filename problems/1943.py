class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        events = defaultdict(int)
        for s, e, c in segments:
            events[s] += c
            events[e] -= c

        res = []
        start, color = None, 0
        for now in sorted(events):
            if start is not None and color != 0: # color == 0 means not painted
                res.append([start, now, color])
            color += events[now]
            start = now
            
        return res