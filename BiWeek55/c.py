import collections as col
import queue 
import sortedcollections as sc
from typing import List

#NOTE: use f2 to change the name of the function to the appropriate name

#NOTE: DONT FORGET TO ADD THE REQUIRED IMPORTS BELOW THIS LINE BEFORE SUBMITTING
#NOTE: code for submission goes below this line ---------------------------------------------------

#NOTE: this is upsolved after looking at others, i choked in the contest :( so sad cause this problem is actualyl easy
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        max_min = (0, 0)
        for num in nums:
            max_min = (
                max(max_min[0], num - max_min[1]),
                min(max_min[1], num - max_min[0])
            )
        return max_min[0]
        
#NOTE: code for submission goes above this line ---------------------------------------------------

#NOTE: testing section ----------------------------------------------------------------------------
# (4,2,5,3), (5,6,7,8), 
tests = [(6,2,1,2,4,5)] #NOTE the tests should be tuples so we can unpack them with the boilerplate loop below
outputs = [] # dont have to use this but its here if needed
for i in range(len(tests)):
    test = Solution().maxAlternatingSum(tests[i])
    print(f'TEST CASE {i}: {test}')

#NOTE: testing section ----------------------------------------------------------------------------