class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.lowest, self.left = 0, None
        def dfs(node, depth):
            if node:
                if depth > self.lowest: self.left, self.lowest = node.val, depth
                l, r = dfs(node.left, depth+1), dfs(node.right, depth+1)
        dfs(root, 1)
        return self.left
            