# actual blackmagic
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res, prev, countDown = 1, 1, 0
        
        for i in range(1, len(ratings)):
            if ratings[i] >= ratings[i-1]:
                if countDown > 0:
                    res += (countDown * (countDown + 1)) // 2
                    if countDown >= prev:
                        res += countDown - prev + 1
                    countDown = 0
                    prev = 1
                prev = 1 if ratings[i] == ratings[i - 1] else prev + 1
                res += prev 
            else:
                countDown += 1
             
        if countDown > 0:
            res += (countDown * (countDown + 1)) // 2
            if countDown >= prev:
                res += countDown - prev + 1
                
        return res