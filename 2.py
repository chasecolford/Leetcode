# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = '', ''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        val = str(int(s1[::-1]) + int(s2[::-1]))[::-1]
        dummy = res = ListNode()
        for char in val:
            res.next = ListNode(int(char))
            res = res.next
        return dummy.next

# pretty ugly :)