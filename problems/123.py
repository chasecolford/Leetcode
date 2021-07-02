# this solution is actual blackmagic
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstBuy, secondBuy, firstProfit, secondProfit = 10**4, 10**4, 0, 0
        for price in prices:
            firstBuy = min(firstBuy, price)
            firstProfit = max(firstProfit, price - firstBuy)
            secondBuy = min(secondBuy, price - firstProfit)
            secondProfit = max(secondProfit, price - secondBuy)
        return secondProfit