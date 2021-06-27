class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")
        res, L = [], len(number)
        for i in range(0, L, 3):
            if L - i == 4: 
                res.extend([number[i:i+2], number[i+2:]])
                break
            else: res.append(number[i:i+3])
        return "-".join(res)