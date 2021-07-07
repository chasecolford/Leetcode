"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        start from each of the nodes traverse up their parents as far as 
        we can. We will store each of the values we see in the parents into a 
        set. Since all of the values are unique, the first time we find a value
        that is already in the set, this is the LCA
        """
        seen = set()
        while q:
            seen.add(q.val)
            q = q.parent
        while p:
            if p.val in seen: return p
            p = p.parent