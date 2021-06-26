# based on larry's solution: https://www.youtube.com/watch?v=uqhK5wOtJdA 
# as I was unaware of SortedList in python
# will do upsolve later for a verbose mergesort solution
# since this is somewhat cheese
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortedList = SortedList()
        counts = [0] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            index = sortedList.bisect_left(nums[i])
            counts[i] = index
            sortedList.add(nums[i])
        return counts
        