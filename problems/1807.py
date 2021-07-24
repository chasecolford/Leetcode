class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        res, i, d = "", 0, {k:v for k, v in knowledge}
        while i < len(s):
            if s[i] == '(':
                key = s[i+1:s.find(')',i,len(s))]
                res += d[key] if key in d else '?'
                i += len(key)+1  
            else: res += s[i]     
            i += 1 
        return res   