class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        FREE is the maximum profit I can have while being free to buy. I am free to buy in the current iteration either because 
        I was free to buy in the previous iteration and did nothing in the current iteration, or I was cooling down in the 
        previous iteration and did nothing in the current iteration. 
        HAVE is the maximum profit I can have while having stock, i.e., I've bought a stock and haven't sold it yet. This happens 
        when I was already holding stock but did not sell in this iteration, or I was free to buy stock last iteration and bought
        the stock in the current iteration.
        COOL is the maximum profit I can have while cooling down. This only happens if I was holding a stock in the previous 
        iteration and sold it in the current iteration.
        """
        free, have, cool = 0, float('-inf'), float('-inf')
        for price in prices:
            free, have, cool = max(free, cool), max(have, free - price), have + price
        return max(free, cool)