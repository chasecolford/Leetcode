class Solution:
    def pushDominoes(self, d: str) -> str:
        d = 'L' + d + 'R'
        res = ""
        i = 0
        for j in range(1, len(d)):
            if d[j] == '.':
                continue
            middle = j - i - 1
            if i:
                res += d[i]
            if d[i] == d[j]:
                res += d[i] * middle
            elif d[i] == 'L' and d[j] == 'R':
                res += '.' * middle
            else:
                res += 'R' * (middle / 2) + '.' * (middle % 2) + 'L' * (middle / 2)
            i = j
        return res

# class Solution:
#     def pushDominoes(self, dom: str) -> str:
#         dom = "L" + dom + "R"
#         n, l, res = len(dom), 0, ""
        
#         for r in range(1, n):
#             diff = r - l - 1
#             if dom[r] == ".": continue
            
#             if dom[r] == dom[l]: res += dom[r]*diff     
#             elif dom[r] == "L" and dom[l] == "R":
#                 m, d = divmod(diff, 2)
#                 res += "R"*m + "."*d + "L"*m
#             else: res += "."*diff
                
#             res += dom[r]
#             l = r
        
#         return res[:-1]