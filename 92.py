# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        # null or only 1 element to reverse -> just return the head
        if not head or left == right: 
            return head
        
        p = dummy = ListNode()
        dummy.next = head
        
        # move p to the right spot
        for _ in range(left - 1): 
            p = p.next
        tail = p.next
        
        # reverse the specified section
        for _ in range(right - left):
            temp = p.next                  
            p.next = tail.next            
            tail.next = tail.next.next    
            p.next.next = temp
            
        return dummy.next