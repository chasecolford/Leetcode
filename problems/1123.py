# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.lca, self.deepest = None, 0
        def dfs(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node: return depth
            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)
            if left == right == self.deepest: self.lca = node
            return max(left, right)
        dfs(root,0)
        return self.lca