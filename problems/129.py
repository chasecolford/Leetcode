# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, num):
            if node:
                val = num + str(node.val)
                if not node.left and not node.right: self.res += int(val)
                dfs(node.left, val)
                dfs(node.right, val)
        dfs(root, "")
        return self.res