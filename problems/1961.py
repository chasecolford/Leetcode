class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        temp = ""
        for word in words:
            temp += word
            if temp == s: return True
        return False