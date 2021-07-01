# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # if both nodes are null at the same point, this is fine -> return true
        if not q and not p: return True
        
        # if only one of the nodes is null here, this is not fine -> return false
        elif not p or not q: return False
        
        # if the nodes dont have the same values, this is not fine -> return false
        elif p.val!=q.val: return False
        
        # else, everything is fine -> continue dfs searching and return bool(left dfs AND right dfs)
        else: return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)