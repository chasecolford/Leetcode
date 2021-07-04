# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, summy: int) -> bool:
        if not root: return False
        if not root.left and not root.right and root.val == summy: return True
        summy -= root.val
        return self.hasPathSum(root.left, summy) or self.hasPathSum(root.right, summy)