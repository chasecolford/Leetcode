class SparseVector:
    def __init__(self, nums: List[int]):
        self.dict = {i: x for i, x in enumerate(nums) if x}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum([x * y for i, x in self.dict.items() for j, y in vec.dict.items() if i == j])