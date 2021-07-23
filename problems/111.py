# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        self.res = float('inf')
        def dfs(node, depth):
            if node:
                if not node.left and not node.right:
                    self.res = min(self.res, depth)
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        
        if not root: return 0
        dfs(root, 1)
        return self.res