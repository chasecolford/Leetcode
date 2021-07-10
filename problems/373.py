# will come back for optimal solution another time
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        # contest solution
        return sorted(itertools.product(nums1, nums2), key=sum)[:k]