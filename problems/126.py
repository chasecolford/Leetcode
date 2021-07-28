from collections import defaultdict as dd
class Solution:
    def findLadders(self, begin: str, end: str, wordList: List[str]) -> List[List[str]]:
        tree, words, n = dd(set), set(wordList), len(begin)
        if end not in words: return []
        found, bq, eq, nq, rev = False, {begin}, {end}, set(), False
        while bq and not found:
            words -= set(bq)
            for x in bq:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                    if y in words:
                        if y in eq: found = True
                        else: nq.add(y)
                        tree[y].add(x) if rev else tree[x].add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq): 
                bq, eq, rev = eq, bq, not rev
                
        def backtrack(x): return [[x]] if x == end else [[x] + rest for y in tree[x] for rest in backtrack(y)]
        
        return backtrack(begin)