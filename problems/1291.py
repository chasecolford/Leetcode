class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # joke solution
        a = [12, 23, 34, 45, 56, 67, 78, 89, 
            123, 234, 345, 456, 567, 678, 789, 
            1234, 2345, 3456, 4567, 5678, 6789,
            12345, 23456, 34567, 45678, 56789,
            123456, 234567, 345678, 456789,
            1234567, 2345678, 3456789,
            12345678, 23456789,
            123456789
            ]
        return [x for x in a if low <= x <= high]
        
        # the real solution is actually quite nice
#         sample = "123456789"
#         n = 10
#         nums = []

#         for length in range(len(str(low)), len(str(high)) + 1):
#             for start in range(n - length):
#                 num = int(sample[start: start + length])
#                 if num >= low and num <= high:
#                     nums.append(num)
        
#         return nums