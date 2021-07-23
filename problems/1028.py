# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, trav: str) -> TreeNode:
        stack, i, n = [], 0, len(trav)
        while i < n:
            num, depth = "", 0
            while i < n and trav[i] == '-': 
                depth, i = depth+1, i+1
            while i < n and trav[i] != '-':
                num, i = num+trav[i], i+1
            while len(stack) > depth:
                stack.pop()
            
            node = TreeNode(num)
            if stack and stack[-1].left is None: stack[-1].left = node
            elif stack: stack[-1].right = node
            stack.append(node)
            
        return stack[0]     
            