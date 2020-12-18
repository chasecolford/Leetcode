"""
Given two arrays, write a function to compute their intersection.
"""
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         # bruteforce
#         res = []
#         for i in nums1:
#             if i in nums2:
#                 nums2.remove(i)
#                 res.append(i)
#         return res

# better -> @StefanPochmann
import collections
def intersect(nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    return list((a & b).elements())

print(intersect([1,2,2,2,3,4,5], [6,5,3,2,2,2]))
