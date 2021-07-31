class Solution:
    def queryString(self, s: str, n: int) -> bool:
        return all(re.search(bin(i)[2:],s) for i in range(1,n+1))