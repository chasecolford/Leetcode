"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""
from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root:
            self.res.append(root.val)
            self.dfs(root.left)
            self.dfs(root.right)

    # -----------------------------------------------------------
    # Reference code from others, different ways to do same thing
    #------------------------------------------------------------

    # def preorderTraversal(self, root):
    #     stack, res = [root], []
    #     while stack:
    #         node = stack.pop()
    #         if node:
    #             res.append(node.val)
    #             stack.append(node.right)
    #             stack.append(node.left)
    #     return res

    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     self.ans=[]
    #     def preorder(root):
    #         if root is None:
    #             return
    #         self.ans.append(root.val)
    #         preorder(root.left)
    #         preorder(root.right)
    #     preorder(root)
    #     return self.ans
        
if __name__ == '__main__':
    s = Solution()
    print(s.preorderTraversal(TreeNode(1, right=TreeNode(2, left=TreeNode(3)))))