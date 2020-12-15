"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
"""
class Solution:
    # def maxDepth(self, root: 'Node') -> int:
    #     if not root: return 0
    #     self.depth = 1
    #     self.dfs(root, 1)
    #     return self.depth

    # def dfs(self, root, depth):
    #     if depth > self.depth: self.depth = depth
    #     for child in root.children:
    #         self.dfs(child, depth+1)
            
    def maxDepth(self, root):
        if not root: return 0
        height = 0
        for child in root.children:
            height = max(self.maxDepth(child), height)
        return height + 1