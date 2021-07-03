# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        """
        since we can only make one cut in the tree, we know that
        the sums must be half of the total sum of the tree each.
        i.e., sum(tree) // 2 = sum(partition1) = sum(partition2)
        thus, we make a set and store the sums of all the subtree
        along the way of a normal dfs, so long as the node is not
        the root itself, since the entire subtree doesnt count here
        then, at the end, if half of the total sum is in the set,
        return true, else return false
        """
        def dfs(node):
            if not node: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            if node is not root: sums.add(s)
            return s
        sums = set()
        return dfs(root) / 2 in sums