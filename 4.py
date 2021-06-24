class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        
        # get the lengths and ensure we are working with the smaller array
        shorter, longer = len(A), len(B)
        if shorter > longer: shorter, longer, A, B = longer, shorter, B, A
            
        # binary search helpers low and high, + the math for the size of the left
        # partition, as well as the total length of the arrays when combined.
        # this allows us to logically calculate the partition "cut" points in the 
        # larger array, while only traversing the smaller of the two, hence: O(log(min(A,B)))
        # also, we declare two helper int values for max and min, which are used for the 
        # edge cases when we would have an empty section (min if on left, max if on right)
        IMIN, IMAX = -2**64, 2**64
        low, high = 0, shorter
        leftPartitionSize = (shorter + longer + 1) // 2

        # begin binary search 'on the smaller'
        while low <= high:
            
            # get the partition points for each, where we use the above formula to logcially
            # determine the partition location in the longer array based only on the position in the shorter
            p1, p2 = (low + high) // 2, leftPartitionSize - p1

            # get the main 4 numbers, which are the values on each side
            # of the partition 'cut' positions on each of the arrays
            leftA = A[p1 - 1] if p1 > 0 else IMIN
            leftB = B[p2 - 1] if p2 > 0 else IMIN
            rightA = A[p1] if p1 < shorter else IMAX
            rightB = B[p2] if p2 < longer else IMAX
            
            # leftA is too large, move binary search to the left (high = p1 - 1)
            if leftA > rightB: high = p1 - 1
                
            # leftB is too large, move binary search to the right (lo = p1 + 1)
            elif leftB > rightA: low = p1 + 1
            
            # else, we have found the right partition location, which means we have satisfied:
            # leftA <= rightB and leftB <= rightA
            else:
                
                # if the total length is odd, we simply return max(leftPartition)
                if (shorter + longer) % 2: return max(leftA, leftB)
                    
                # else if the total length is even, we need to return the (max(leftPartition) + min(rightPartition)) / 2
                else: return (max(leftA, leftB) + min(rightA, rightB)) / 2
                    