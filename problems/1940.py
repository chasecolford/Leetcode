class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        """
        if a value appears in all of the arrays, and they are all strictly increasing,
        then this value must appear exactly len(arrays) times in total.
        thefore, we can just use counter.
        """
        counts = Counter(val for arr in arrays for val in arr)
        res = []
        for val, count in counts.items():
            if count == len(arrays): res.append(val)
        return res