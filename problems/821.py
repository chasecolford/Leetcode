class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        """
        Find the locations of all char C in S and logically fill in the gaps between them
        """
        n = len(S) 
        pos = -float('inf')
        answer = [n] * n
        
        for i in range(n):
            if S[i] == C:
                pos = i
            answer[i] = i - pos
            
        for j in range(n)[::-1]:
            if S[j] == C:
                pos = j
            answer[j] = min(answer[j], abs(j - pos))
        
        return answer