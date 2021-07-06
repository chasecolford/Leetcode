class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        """
        According to Xor property
        The inverse is XOR!
        If you have:
        c = a^b;
        You can get a or b back if you have the other value available:
        a = c^b; // or b^c (order is not important)
        b = c^a; // or a^c
        """
        res = [first]
        for e in encoded:
            res.append(res[-1] ^ e)
        return res