class Solution:
    def printVertically(self, s: str) -> List[str]:
        cols = s.split()
        rows = itertools.zip_longest(*cols, fillvalue=' ')
        return [''.join(row).rstrip() for row in rows]