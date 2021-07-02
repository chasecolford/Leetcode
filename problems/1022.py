# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node):
            if not node.right and not node.left: self.res += node.val
            if node.left:
                node.left.val += 2 * node.val
                dfs(node.left)
            if node.right:
                node.right.val += 2 * node.val
                dfs(node.right)
                
        self.res = 0
        dfs(root)
        return self.res