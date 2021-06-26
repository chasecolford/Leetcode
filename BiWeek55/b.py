import collections as col
import queue 
import sortedcollections as sc
from typing import List

#NOTE: use f2 to change the name of the function to the appropriate name

#NOTE: DONT FORGET TO ADD THE REQUIRED IMPORTS BELOW THIS LINE BEFORE SUBMITTING
#NOTE: code for submission goes below this line ---------------------------------------------------

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        last = ""
        while True:
            s = s.replace(part, "", 1)
            if s == last: break
            last = s
        return s
        
#NOTE: code for submission goes above this line ---------------------------------------------------

#NOTE: testing section ----------------------------------------------------------------------------

tests = [("daabcbaabcbc", "abc"), ("axxxxyyyyb", "xy")] #NOTE the tests should be tuples so we can unpack them with the boilerplate loop below
outputs = [] # dont have to use this but its here if needed
for i in range(len(tests)):
    test = Solution().removeOccurrences(*(tests[i]))
    print(f'TEST CASE {i}: {test}')

#NOTE: testing section ----------------------------------------------------------------------------