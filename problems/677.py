class MapSum:
    def __init__(self): self.mappy = {}
    def insert(self, key: str, val: int) -> None: self.mappy[key] = val
    def sum(self, prefix: str) -> int: return sum((val for key, val in self.mappy.items() if key.startswith(prefix)))
