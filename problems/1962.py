class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = [-val for val in piles]
        heapify(h)
        for i in range(k):
            cur = -heappop(h)
            cur = cur - (cur // 2)
            heappush(h, -cur)
        return -sum(h)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # too slow
        # piles.sort()
        # for i in range(k):
        #     cur = piles.pop()
        #     cur -= cur // 2
        #     insort(piles, cur)
        # return sum(piles)