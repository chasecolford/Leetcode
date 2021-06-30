# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        preorder traversal
        if we find either of the nodes we are looking for, 
        we return the value to the parent node.
        if any given node ever gets 2 non-null values,
        it means this node is the LCA.
        Lastly, a small optimization is that if we find the LCA,
        we can return this value to the parent. If a node is getting
        a value that is not null and is not one of the two nodes
        we were searching for, per our implementation, this means that
        it will be the LCA node, so we can continue returning it up the stack.
        """
        def preorder(node, targets):
            if not node: return None
            if node in targets: return node
            
            left = preorder(node.left, targets)
            right = preorder(node.right, targets)
            
            if left and right: return node
            elif left: return left
            elif right: return right
            else: return None
        
        return preorder(root, (p, q))