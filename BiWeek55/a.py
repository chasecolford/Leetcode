import collections as col
from math import fabs
import queue 
import sortedcollections as sc
from typing import List

#NOTE: use f2 to change the name of the function to the appropriate name

#NOTE: DONT FORGET TO ADD THE REQUIRED IMPORTS BELOW THIS LINE BEFORE SUBMITTING
#NOTE: code for submission goes below this line ---------------------------------------------------
#upsolved for cleaner code, based on FACEPLANTS clean solution
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        flag = 0
        nums = [0] + nums + [1001]
        for i in range(len(nums) - 3):
            if nums[i + 1] >= nums[i + 2]:
                if flag:
                    return False
                if nums[i] >= nums[i + 2] and nums[i + 1] >= nums[i + 3]:
                    return False
                flag = 1
        return True
        
#NOTE: code for submission goes above this line ---------------------------------------------------

#NOTE: testing section ----------------------------------------------------------------------------

tests = [(1,2,10,5,7), (2,3,1,2), (1,1,1), (1,2,3)] #NOTE the tests should be tuples so we can unpack them with the boilerplate loop below
outputs = [] # dont have to use this but its here if needed
for i in range(len(tests)):
    test = Solution().canBeIncreasing(tests[i])
    print(f'TEST CASE {i}: {test}')

#NOTE: testing section ----------------------------------------------------------------------------