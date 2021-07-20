class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res, i, n = 0, 1, len(arr)
        while i < n:
            while i < n and arr[i-1] == arr[i]: i+=1
                
            up = 0
            while i < n and arr[i-1] < arr[i]:
                up += 1
                i += 1
                
            down = 0
            while i < n and arr[i-1] > arr[i]:
                down += 1
                i += 1
                
            if up > 0 and down > 0: res = max(res, up + down + 1)
                
        return res