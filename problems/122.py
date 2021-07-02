class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        since buying low and holding until the highes point is logically
        the same as buying and selling everytime day i is less than day i+1,
        we can just add those profits individually. Also, we just max this with
        0 so that we dont reduce our total whenever the price goes down
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))