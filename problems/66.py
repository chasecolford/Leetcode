class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        # cursed solution
        # return [int(x) for x in str(int("".join([str(c) for c in d]))+1)]
        
        # "real" solution
        for i in range(len(d)-1, -1, -1):
            if d[i] == 9: d[i] = 0; 
            else: d[i]+=1; return d
        return [1] + d