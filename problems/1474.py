# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        while cur:
            
            count = 1
            while cur and count < m:
                cur = cur.next
                count += 1
                
            count = 0
            while cur and cur.next and count < n:
                cur.next = cur.next.next
                count += 1
                
            if cur: cur = cur.next
                
        return head