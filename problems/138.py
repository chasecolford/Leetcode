class Solution(object):
    def copyRandomList(self, head):
        if not head: return
        old, new = head, Node(head.val, None, None)
        visited = {old: new}
        clone = lambda x : visited.setdefault(x, Node(x.val, None, None)) if x else None
        while old:
            new.random, new.next = clone(old.random), clone(old.next)
            old, new = old.next, new.next
        return visited[head]