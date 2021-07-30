class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def dfs(node):
            if not root: return [0, 0]
            inr = dcr = 1
            if node.left:
                left = dfs(node.left)
                if (node.val == node.left.val + 1): dcr = left[1] + 1
                elif (node.val == node.left.val - 1): inr = left[0] + 1
            
            if node.right:
                right = dfs(node.right)
                if (node.val == node.right.val + 1): dcr = max(dcr, right[1] + 1)
                elif (node.val == node.right.val - 1): inr = max(inr, right[0] + 1)
                    
            self.res = max(self.res, dcr + inr - 1)
            return [inr, dcr]
        
        self.res = 0
        dfs(root)
        return self.res