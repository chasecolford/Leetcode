# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # main idea -> dfs the tree normally with the extra param
        # of passing the largest seen node into the dfs function
        def dfs(node, largest):
            if not node: return 0
            mx = max(node.val, largest)
            return (node.val >= largest) + dfs(node.left, mx) + dfs(node.right, mx)
        return dfs(root, -10**4-1)
        

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, mx):
            if node:
                if node.val >= mx: self.res += 1
                dfs(node.left, max(node.val, mx))
                dfs(node.right, max(node.val, mx))
        dfs(root, root.val)
        return self.res