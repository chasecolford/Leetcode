class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        
        #sort
        arr.sort()
        
        #find min
        answer = []
        smallest = 1000001 #-10^6 <= arr[i] <= 10^6
        for i in range(len(arr) - 1):
            if abs(arr[i+1] - arr[i]) < smallest:
                smallest = abs(arr[i+1] - arr[i])
        
        #find all pairs that match min
        for i in range(len(arr) - 1):
            if abs(arr[i+1] - arr[i]) == smallest:
                answer.append([arr[i], arr[i+1]])
                
        return answer