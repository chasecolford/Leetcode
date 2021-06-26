class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        left = nums[:n]
        right = nums[n:]
        answer = [] # * 2n
        for i in range(n):
            answer.append(left[i])
            answer.append(right[i])
        return answer