class Solution:
    def expand(self, s: str) -> List[str]:        
        
        def backtrack(start, string):
            if start == n: return res.append(string)
            if s[start] == '{':
                brace = s[start+1 : s.find('}', start, n)]
                for letter in brace.split(','): 
                    backtrack(start + len(brace) + 2, string+letter)
            else: backtrack(start + 1, string + s[start])
             
        res, n = [], len(s)
        backtrack(0, "")
        return sorted(res)