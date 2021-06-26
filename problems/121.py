"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), design an 
algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""
#NOTE: we can just track the smallest value we have seen to 'i',
# then compare the profit we could make to some global and store max

def maxProfit(prices):
    maxProf, minPrice = 0, float('inf')
    for price in prices:
        if price < minPrice: minPrice = price
        prof = price - minPrice
        if prof > maxProf: maxProf = prof
    return maxProf

#expected 5
print(maxProfit([7,1,5,3,6,4]))
"""NOTE:
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Not 7-1 = 6, as selling price needs to be larger than buying price.
"""