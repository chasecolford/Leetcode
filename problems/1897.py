class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return all([x % len(words) == 0 for x in collections.Counter(''.join(words)).values()])
