class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        startHour, startMin = map(int, startTime.split(':'))
        finishHour, finishMin = map(int, finishTime.split(':'))
        
        def fullPlayed(sh, sm, fh, fm):
            res = (fh - sh - 1) * 4 + fm // 15 + (60 - sm) // 15
            res = max(res, 0)
            return res
        
        if startTime > finishTime: return fullPlayed(startHour, startMin, 23, 60) + fullPlayed(0, 0, finishHour, finishMin)
        else: return fullPlayed(startHour, startMin, finishHour, finishMin)