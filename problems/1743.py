class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        """
        find the nodes that appear only once in the pairs, since 
        these will be the first and last nodes
        
        we can just choose either of these as the start and find the 
        next pair that has the needed value. since we know the direction of this 
        pair, we know the direction of the next, and so on.
        
        basically, form adj matrix, find start, dfs.
        """
        res, seen = [], set()  
        
        # dfs
        def dfs(num):
            seen.add(num)
            for nx in adj[num]:
                if nx not in seen: dfs(nx)
            res.append(num) 
            
        # build adjacency matrix
        adj = defaultdict(list)
        for a, b in pairs:
            adj[a].append(b)
            adj[b].append(a)

		# locate start and begin dfs
        for k, v in adj.items():
            if len(v) ==1:
                dfs(k)
                break
            
        return res