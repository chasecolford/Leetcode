"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

 

Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5

"""
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        ans.insert(0, -1)
        prevmax = arr[-1] #print: 1, 6, 4, 5, 18, 17
        for i in range(len(arr)-1, 0, -1): #6(inclusive), -1(exclusive), step -1
            if arr[i] > prevmax:
                prevmax = arr[i]
            ans.insert(0, prevmax)
        return ans 