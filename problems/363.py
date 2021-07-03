# the optimized impl of this problem is currently above my paygrade, but we had to do it for the july challenge
class Solution:
    def maxSumSubmatrix(self, matrix, k):
        
        # helper that handles the 1d case and returns the max
        def maxSumSubarray(arr):
            subMax, cur, prefixSums = float('-inf'), 0, [float('inf')]
            for x in arr:
                bisect.insort(prefixSums, cur) # as others have noted, insort is O(n) here
                cur += x
                i = bisect.bisect_left(prefixSums, cur - k)
                subMax = max(subMax, cur - prefixSums[i])
            return subMax
        
        # calculate the prefix sums
        m, n = len(matrix), len(matrix[0])
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y+1] += matrix[x][y]
        
        # like in this video: https://www.youtube.com/watch?v=yCQN096CwWM
        # we need to iterate through all the columns, calling 
        # our maxSumSubarray each time
        res = float('-inf')
        for y1 in range(n):
            for y2 in range(y1, n):
                arr = []
                for z in range(m):
                    arr.append(matrix[z][y2] - (matrix[z][y1-1] if y1 > 0 else 0))
                res = max(res, maxSumSubarray(arr))
                
        return res