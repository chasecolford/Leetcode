class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, counts, running = 0, {0:1}, 0
        for num in nums:
            running += num
            if (running - k) in counts: res += counts[running - k]
            if running in counts: counts[running] += 1
            else: counts[running] = 1
        return res
