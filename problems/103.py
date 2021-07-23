# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.levels = []
        def dfs(node, depth):
            if node:
                if depth+1 > len(self.levels):
                    self.levels.append([])
                self.levels[depth].append(node.val)
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        
        dfs(root, 0)
        
        res = []
        flag = True   
        for level in self.levels:
            if flag: res.append(level)
            else: res.append(level[::-1])
            flag = not flag
        return res