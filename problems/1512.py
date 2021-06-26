class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 1 <= nums.length <= 100
        # 1 <= nums[i] <= 100
        #count each number, assign it to bin, loop bin, calculate permutations, return sum of this
        pairs = 0
        bins = [0] * 100
        for i in nums:
            bins[i-1]+=1
        
        for b in bins:
            pairs += (b * (b - 1) / 2)
        
        return pairs