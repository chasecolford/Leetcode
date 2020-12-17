"""
Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.

Return a list of two integers [A, B] where:

    A and B are No-Zero integers.
    A + B = n

It's guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.
"""
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            if '0' not in f'{i}{n-i}':
                return [i, n-i]

    # cool generator idea (from @StefanPochmann)
    # return next([a, n-a] for a in range(n) if '0' not in f'{a}{n-a}')