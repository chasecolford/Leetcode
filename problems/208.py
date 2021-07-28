class Trie:
    def __init__(self): self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur: cur[char] = {}
            cur = cur[char]
        cur['.'] = '\0'

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur: return False
            cur = cur[char]
        return '.' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur: return False
            cur = cur[char]
        return True
    