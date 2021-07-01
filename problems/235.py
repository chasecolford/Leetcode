# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # this approach simply 'walks' down the tree from root -> lca, which is found
        # when the 'side' of the node that p and q are on become different (i.e., when paths diverge)
        
        # # iterative
        # while root:
        #     if max(p.val, q.val) < root.val: root = root.left
        #     elif min(p.val, q.val) > root.val: root = root.right
            
        # recursive
        if not root: return None
        if max(p.val, q.val) < root.val: return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val: return self.lowestCommonAncestor(root.right, p, q)
        return root
    