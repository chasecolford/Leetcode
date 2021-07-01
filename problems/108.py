# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) > 0:
            i = len(nums) // 2
            node = TreeNode(nums[i])
            
            node.left = self.sortedArrayToBST(nums[:i])
            node.right = self.sortedArrayToBST(nums[i+1:])
            
            return node
        
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         def makeTree(left, right):
#             if left > right: 
#                 return None
#             mid = (left + right) // 2
#             node = TreeNode(nums[mid])
#             node.left = makeTree(left, mid - 1)
#             node.right = makeTree(mid + 1, right)
#             return node
#         return makeTree(0, len(nums) - 1)

#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         def makeBST(l, r):
#             if l > r: return None
#             mid = (l + r) // 2
#             node = TreeNode(nums[mid])
#             node.left = makeBST(l, mid - 1)
#             node.right = makeBST(mid + 1, r)
#             return node
#         return makeBST(0, len(nums) - 1)
        