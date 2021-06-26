"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if root:
            self.res.append(root.val)
            for child in root.children:
                self.dfs(child)

"""
Follow up:

Recursive solution is trivial, could you do it iteratively?
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res, q = [], root and [root]
        while q:
            node = q.pop()
            res.append(node.val)
            q.extend([n for n in reversed(node.children) if n])  
        return res