class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        """
        brute force? only 8
        """
        def scr(s, m):
            score = 0
            for i in range(len(s)):
                if s[i] == m[i]: score += 1
            return score
        
        res, l = 0, len(students)
        for perm in permutations(range(l), l):
            temp = 0
            for i, j in enumerate(perm):
                temp += scr(students[i], mentors[j])
            res = max(res, temp)
        return res