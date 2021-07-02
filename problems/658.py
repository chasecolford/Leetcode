class Solution:
    def findClosestElements(self, arr: List[int], k: int, target: int) -> List[int]:
        
        # find the index for target (x)
        l, r = 0, len(arr) - 1 
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] < target: l = m + 1
            else: r = m - 1
        
        # let target index = l after the binary search
        # since this is the index of the target we start from
        targetIndex = l
        
        """
        now that we have found the index of the target element
        we just need to linearly find the k closet to it
        we can do this by checking the right and left, and applying
        |a - x| < |b - x|, or
        |a - x| == |b - x| and a < b
        and updating the right and left pointers accordingly
        """
        l, r = targetIndex, targetIndex
        while r - l < k:
            if l == 0: return arr[:k]
            if r == len(arr): return arr[-k:]
            if target - arr[l - 1] <= arr[r] - target: l -= 1
            else: r += 1
                
        return arr[l:r]
        
            