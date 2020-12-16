"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        else: return self.sym(root.left, root.right)
        
    def sym(self, left, right):
        if not left and not right: return True
        if not left or not right: return False
        
        if left.val == right.val:
            x = self.sym(left.left, right.right)
            y = self.sym(left.right, right.left)
            return x and y
        else: return False