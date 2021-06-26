# based on larry's solution: https://www.youtube.com/watch?v=uqhK5wOtJdA 
# as I was unaware of SortedList in python
# will do upsolve later for a verbose mergesort solution
# since this is somewhat cheese
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortedList = SortedList()
        counts = []
        nums.reverse()
        
        for num in nums:
            index = sortedList.bisect_left(num)
            counts.append(index)
            sortedList.add(num)
        counts.reverse()
        return counts
        