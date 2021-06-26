"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = 0
        self.dfs(root)
        return self.res
    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.dfs(root.right)