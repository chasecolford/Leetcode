class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        def dfs(node, depth):
            if node:
                if depth >= len(res): res.append(node.val)
                elif node.val > res[depth]: res[depth] = node.val
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        
        res = []
        dfs(root, 0)
        return res