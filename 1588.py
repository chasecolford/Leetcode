class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        """
        1 <= arr.length <= 100
        1 <= arr[i] <= 1000
        """
        answer = 0
        l = len(arr)
        
        #generate odd subseq sizes
        
        #maxSub = l - (l % 2)
        
        if l % 2 == 0:
            maxSub = l - 1
        else:
            maxSub = l
        
        #outer loop, step by 2, always odd, up to maxSub (inclusive)
        for i in range(1, maxSub+1, 2):
            
            #loop through arr for every slice of size i
            for j in range(l - i + 1):
                # slice = arr[j:j+i]
                # print(slice)
                answer += sum(arr[j:j+i])
        
        # print(answer)
        return answer