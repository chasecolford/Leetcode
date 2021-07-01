# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def dfs(root):
            if not root: return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            level = max(left, right) + 1
            
            if level > len(res):
                res.append([])
            res[level-1].append(root.val)
            
            return level
        
        res = []
        dfs(root)
        return res