class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        """ explanation from: https://leetcode.com/problems/count-good-numbers/discuss/1314322/C%2B%2B-(-5-even-indices)-*-(4-odd-indices)-with-explanation
        At even indices there can be 5 values(0,2,4,6,8) i.e. all even numbers 0 to 9
        And At odd indices there can 4 values(2,3,5,7) i.e. all prime numbers 0 to 9
        So we notice that there are 5 values which can be in even indices and 4 in odd indices.
        So now Logic is simple :-
        Total number of good digit strings would be  (5 ^ even indices) * (4 ^ odd indices)....We also need to return  % 10^9 + 7.
        But the other problem is the constraints which is way too big. So we need to calculate (5 ^ even indices) and  (4 ^ odd indices) in log(n) time,
        which is done by powerMod function. Now lets understand the powerMod fuction :-
        """
        mod = 10 ** 9 + 7
        return pow(5, (n + 1) // 2, mod) * pow(4, n // 2, mod) % mod