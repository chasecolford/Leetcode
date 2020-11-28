class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for n in nums1:
            added = False
            for i in range(nums2.index(n), len(nums2)):
                if nums2[i] > n:
                    res.append(nums2[i])
                    added = True
                    break
            if not added:
                res.append(-1)
        return res
