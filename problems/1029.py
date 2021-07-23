class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # we can sort the pairs (ai, bi) in cost
        # based on the total 'savings' you save by
        # choosing one over the other. i.e., for
        # the pair (10, 200), we save 190 by choosing 
        # to send the ith person to city b.
        a = [i for i,j in costs]
        diff = [j - i for i,j in costs]
        return sum(a) + sum(sorted(diff)[:len(costs)//2])