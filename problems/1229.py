class Solution:
    def minAvailableDuration(self, s1: List[List[int]], s2: List[List[int]], duration: int) -> List[int]:
        s1.sort()
        s2.sort()
        p1, p2 = 0, 0
        
        while p1 < len(s1) and p2 < len(s2):
            """
            find the common boundary of these two slots:
            this is the max of the start times and the 
            min of the end times.
            """
            r, l = min(s1[p1][1], s2[p2][1]), max(s1[p1][0], s2[p2][0])
            if r - l >= duration: return [l, l + duration]
            
            # incremenet the pointer for the time slot that ends earlier
            if s1[p1][1] < s2[p2][1]: p1 += 1
            else: p2 += 1
        
        return []