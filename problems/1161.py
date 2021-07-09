# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        # dfs version
        levels = defaultdict(int)
        def dfs(root, depth):
            if root:
                levels[depth] += root.val
                dfs(root.left,  depth+1)
                dfs(root.right, depth+1)
			
        dfs(root, 1)
        return max(levels, key=levels.get)