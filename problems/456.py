class Solution:
    def find132pattern(self, nums):
        stack, s3 = [], -float("inf")
        for n in nums[::-1]:
            if n < s3: return True
            while stack and stack[-1] < n: s3 = stack.pop()
            stack.append(n)
        return False
    
    """ EXAMPLE:
    [3,1,4,2][::-1] -> [2,4,1,3]
    iteration 1:
        n = 2
        s3 = -inf
        false
        false: stack = []
        stack = [2]
    iteration 2:
        n = 4
        s3 = -inf
        false
        true: stack[-1] = 2, n = 4, 2 < 4
        s3 = stack.pop() = 2
        stack = [4]
    iteration 3:
        n = 1
        s3 = 2
        true: return True
    """   