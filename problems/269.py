from collections import defaultdict, Counter, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # create the adj list and the indegree counter, start with each indegree = 0
        adj = defaultdict(set)
        indeg = Counter({c : 0 for word in words for c in word})
        
        # now we populate the adj list and the indegrees of the verts (letters)
        for w1, w2 in zip(words, words[1:]):
            for i, j in zip(w1, w2):
                if i != j:
                    if j not in adj[i]:
                        adj[i].add(j)
                        indeg[j] += 1
                    break
            else: # check that the second word isnt a prefix of the first word (i.e., w1 = abcd, w2 = ab)
                if len(w1) > len(w2): return "" # this would be invalid -> return empty string
        
        # now we use BFS (deque) to repeatedly remove nodes that have indegrees of 0
        res = []
        q = deque([i for i in indeg if indeg[i] == 0])
        while q:
            i = q.popleft()
            res.append(i)
            for j in adj[i]:
                indeg[j] -= 1
                if indeg[j] == 0: q.append(j)
        
        # if not all of the unique letters are in the output, return ""
        if len(res) < len(indeg): return ""
        
        # else, we found a valid ordering above, return this ordering as string
        return "".join(res)