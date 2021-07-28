# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        """
        we can dfs, and always return the length of the longest sequence
        up to node[i]. This means that a lead node returns 1, since the sequence
        would just be this node.
        Formally, each stack frame returns:
        if we are a continuation of either node.left or node.right,
        increment left or right by 1. Then, we can return
        max(left, right) if we were a continuation of either,
        else 1, since we are inherently a continuation of ourselves.
        we will always update a class variable self.longest at each step.
        """
        self.res = 0 # store the longest sequence
        def dfs(node):
            if node:
                l = dfs(node.left)
                r = dfs(node.right)
                ret = 0
                if l and r and node.val == node.left.val-1 == node.right.val-1: ret = max(l, r) + 1
                elif l and node.val == node.left.val-1: ret = l + 1
                elif r and node.val == node.right.val-1: ret = r + 1
                else: ret = 1
                self.res = max(self.res, ret)
                return ret
            else: return 0
        dfs(root)
        return self.res