"""
 A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:

Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

Note:
The boundaries of each input argument are 1 <= left <= right <= 10000.
"""
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for num in range(left, right+1): #+1 inclusive upperbound
            strnum = str(num)

            if num < 10: #default cases:
                ans.append(num)
            else:
                flag = True
                for dig in strnum:
                    if int(dig) == 0: #num contains 0
                        flag = False
                        break
                    if num % int(dig) == 0: #num is div by digit
                        continue
                    else: #num not div by digit
                        flag = False
                        break
                if flag:
                    ans.append(num)
        return ans