class Solution:
    def sufficientSubset(self, root, limit):
        if not root.left and not root.right: return None if root.val < limit else root
        if root.left: root.left = self.sufficientSubset(root.left, limit - root.val)
        if root.right: root.right = self.sufficientSubset(root.right, limit - root.val)
        return root if root.left or root.right else None