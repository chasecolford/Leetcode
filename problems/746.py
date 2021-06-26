"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. 
You need to find minimum cost to reach the top of the floor, 
and you can either start from the step with index 0, or the step with index 1. 
"""

#NOTE: we can start at 2 since the first two values are always just themselves,
# where from the third valu (i = 2), we only care about the cheapest to get to it
# i.e., itself + the smallest from (i-1, i-2), one or two steps away behind it.
# the costs accumulate, so we can just add these in place.
def minCostClimbingStairs(cost):
    for i in range(2, len(cost)):
        cost[i] += min(cost[i-1], cost[i-2])
    return min(cost[-1], cost[-2])


#expected 6 -> Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))