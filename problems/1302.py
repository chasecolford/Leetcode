"""
Given a binary tree, return the sum of values of its deepest leaves. 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # gonna clean this up and also do a level order traversal instead
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.depth = 1
        self.maxDepth = 1
        self.sum = 0
        self.dfs(root, 1)
        return self.sum
    def dfs(self, root, depth):
        if root:
            if depth == self.maxDepth:
                self.sum += root.val
            elif depth > self.maxDepth:
                self.maxDepth = depth
                self.sum = root.val
            self.dfs(root.left, depth + 1)
            self.dfs(root.right, depth + 1)
    
        
            