class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        answer = 0
        l = len(arr)
        for i in range(l):
            for j in range(i+1, l):
                for k in range(j+1, l):
                    if abs(arr[i] - arr[j]) <= a:
                        if abs(arr[j] - arr[k]) <= b:
                            if abs(arr[i] - arr[k]) <= c:
                                answer += 1
        return answer