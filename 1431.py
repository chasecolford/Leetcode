class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        m = max(candies)
        answer = []
        for i in candies:
            if i + extraCandies >= m:
                answer.append(True)
            else:
                answer.append(False)
        return answer
        
        # return [i >= (max(candies) - extraCandies) for i in candies]