class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # make custom map of the order of the 26 letters, where the
        # key is 1-26 and the value is the letter 
        # the we sort based on the key, and later build the string based on the 
        # letter associated with each key
        key = {order[i]: i for i in range(len(order))}
        sections = [""] * 27
        for char in s:
            if char in key: sections[key[char]] += char
            else: sections[-1] += char
        return "".join(sections)