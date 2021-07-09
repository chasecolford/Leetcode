"""
faster version: based on the following but with the addition of binary search
Approach 2: Intelligently Build a Subsequence

Intuition

As stated in the previous approach, the difficult part of this problem is deciding if an 
element is worth using or not. Consider the example nums = [8, 1, 6, 2, 3, 10]. Let's try 
to build an increasing subsequence starting with an empty one: sub = [].

    At the first element 8, we might as well take it since it's better than nothing, so sub = [8].

    At the second element 1, we can't increase the length of the subsequence since 8 >= 1, so we have
    to choose only one element to keep. Well, this is an easy decision, let's take the 1 since there 
    may be elements later on that are greater than 1 but less than 8, now we have sub = [1].

    At the third element 6, we can build on our subsequence since 6 > 1, now sub = [1, 6].

    At the fourth element 2, we can't build on our subsequence since 6 >= 2, but can we improve on it 
    for the future? Well, similar to the decision we made at the second element, if we replace the 6 with 2, 
    we will open the door to using elements that are greater than 2 but less than 6 in the future, so sub = [1, 2].

    At the fifth element 3, we can build on our subsequence since 3 > 2. Notice that this was only possible 
    because of the swap we made in the previous step, so sub = [1, 2, 3].

    At the last element 10, we can build on our subsequence since 10 > 3, giving a final subsequence 
    sub = [1, 2, 3, 10]. The length of sub is our answer.

It appears the best way to build an increasing subsequence is: for each element num, if num is greater than 
the largest element in our subsequence, then add it to the subsequence. Otherwise, perform a linear scan 
through the subsequence starting from the smallest element and replace the first element that is greater 
than or equal to num with num. This opens the door for elements that are greater than num but less than the 
element replaced to be included in the sequence.

One thing to add: this algorithm does not always generate a valid subsequence of the input, but the length 
of the subsequence will always equal the length of the longest increasing subsequence. For example, with the 
input [3, 4, 5, 1], at the end we will have sub = [1, 4, 5], which isn't a subsequence, but the length is 
still correct. The length remains correct because the length only changes when a new element is larger than 
any element in the subsequence. In that case, the element is appended to the subsequence instead of 
replacing an existing element.

Algorithm

    Initialize an array sub which contains the first element of nums.

    Iterate through the input, starting from the second element. For each element num:
        If num is greater than any element in sub, then add num to sub.
        Otherwise, iterate through sub and find the first element that is greater than or equal to num. 
        Replace that element with num.

    Return the length of sub.

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # binary search helper
        def bsearch(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target: return mid
                if arr[mid] > target: right = mid - 1
                else: left = mid + 1
            return left
                
        sub = []
        for num in nums:
            i = bsearch(sub, num)
            if i == len(sub): sub.append(num)
            else: sub[i] = num
        return len(sub)
        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        naive: n^2 with dp
        outer loop i from 1, len(nums)
        inner loop fro 0, i
        if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j] + 1)
        return the max of dp
        
        not sure about nlogn yet
        seems it needs this (or something like it): https://en.wikipedia.org/wiki/Patience_sorting
        """
        if not nums: return 0
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)
                