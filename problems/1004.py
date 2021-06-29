class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Input:   k = 3
        Nums =   [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        Section: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
        Output:  10
        """
        # insanely concise one pass sliding window solution upsolved
        # after reading lee's solution

        # left and right represent the bounds of the current MAX lengh
        # sliding window found. It is important to note that at any given point,
        # left and right do not actually represent the longest range; instead,
        # left and right will always be [LONGEST_WINDOW_FOUND] apart, which means
        # at the end of the function, we simply return left - right + 1.
        # furthermore, if k < 0, we know that this is not a valid range, so we simply
        # move the entire window over one unit (and adjust k based on the value at left)
        # the same logic applies when we change k initially, where it changes based on
        # the current value in nums at the index of the right window
        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left + 1