class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        self.res = []
        def dfs(node, path, val):
            if node:
                if (node.left == node.right == None) and node.val + val == target: 
                    self.res.append(path + [node.val])
                dfs(node.left, path + [node.val], val + node.val)
                dfs(node.right, path + [node.val], val + node.val)
        dfs(root, [], 0)
        return self.res