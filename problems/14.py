class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        while True:
            try: res += strs[0][len(res)] if all(strs[i][len(res)] == strs[0][len(res)] for i in range(len(strs))) else 1
            except: return res