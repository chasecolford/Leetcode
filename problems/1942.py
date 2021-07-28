class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        for index, (start, end) in enumerate(times):
            events.append((start, True, index))
            events.append((end, False, index))
        
        available, assigned = list(range(len(times))), {}
        for time, arriving, index in sorted(events):
            if arriving:
                assigned[index] = heappop(available)
                if index == targetFriend: return assigned[index]
            else: heappush(available, assigned[index])