class Solution:
    def twoEggDrop(self, n: int) -> int:
        # https://brilliant.org/wiki/egg-dropping/#2-eggs-k-floors
        return ceil((-1+sqrt(1+8*n))/2)