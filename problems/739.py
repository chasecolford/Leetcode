class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        """ Monostack O(N)
        goal: preserve the invariant of the monostack, where for each new item, we
        remove all items that are smaller than this item (keeping track of the index).
        we will also start from the back of the temps list.
        """
        res, stack = [0]*len(temps), [len(temps)-1] # the last element is always 0, since there are no more days
        for i in range(len(temps)-2,-1,-1):
            while stack and temps[stack[-1]] <= temps[i]: stack.pop()
            res[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return res