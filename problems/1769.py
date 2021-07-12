class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        two pass O(n):
        iterate from left to right,
        iterate from right to left,
        during each of these, we keep track of how many turns it would
        take to move all the balls on the (right or left) of ball i 
        into the ith bin.
        summing these together gives us the total
        """
        n = len(boxes)
        res = [0] * n
        balls, ops = 0, 0
        for i in range(n):
            res[i] += ops
            balls += int(boxes[i])
            ops += balls
        balls, ops = 0, 0
        for i in range(n-1,-1,-1):
            res[i] += ops
            balls += int(boxes[i])
            ops += balls
        return res
