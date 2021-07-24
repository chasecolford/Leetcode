# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        """
        since all values are unique and we only visit each once in our dfs,
        we actually never need to compare the nodes directly, only count the
        amount of times we see a node that is in the nodes list.
        each node will return the total nodes in its subtree that are in nodes.
        at a given node, if l + r == len(nodes), we are done (this could include the node itself)
        """
        self.lca = None
        goal, nodes = len(nodes), set([x.val for x in nodes])
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if l+r+(node.val in nodes) == goal and not self.lca: self.lca = node
            return l + r + (node.val in nodes)
        dfs(root)
        return self.lca