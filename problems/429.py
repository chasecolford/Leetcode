class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        res, q = [], deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                q.extend(node.children)
            res.append(level)
        return res
                