"""
Find the sum of all left leaves in a given binary tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        return self.res
    def dfs(self, root):
        if root:
            if root.left and not root.left.left and not root.left.right:
                self.res += root.left.val
            self.dfs(root.left)
            self.dfs(root.right)