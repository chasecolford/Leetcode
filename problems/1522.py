class Solution:
    def diameter(self, root: 'Node') -> int:
        if not root: return 0
        def dfs(node):
            if not node.children: return 1
            a = b = 0
            for n in node.children: a, b = sorted([a, b, dfs(n)])[-2:]
            self.res = max(self.res, a+b)
            return max(a, b) + 1
        
        self.res = 0
        dfs(root)
        return self.res
    
    
        """ Alternative code for the 1 line compressed for loop
        Normal:
        x = dfs(n)
        if x > a: a, b = x, a
        elif x > b: b = x
        
        Stupid:
        x = dfs(n)
        a, b = (x, a) if (x > a) else (a, x) if (x > b) else (a, b)
        """