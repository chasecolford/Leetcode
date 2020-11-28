class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = len(arr)
        last = 0
        count = 0
        for i in range(l):
            if last == arr[i]:
                count += 1
            else:
                count = 1
            last = arr[i]
            if float(count) / float(l) > .25:
                return arr[i]
        return -1