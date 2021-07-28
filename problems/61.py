# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """ Main idea:
        First, calculate the mod of k % len(list) if k >= len(list),
        since k can be much larger than the length of the list. This
        saves us a lot of repeated work in the worst case.
        
        Then, there are only 3 steps:
        1. Find the (k+1)th node from the back and make it point to None
        2. Make the last node point to the head
        3. Return the kth node from the back, since this is the new head
        """
        
        if not head: return
        
        # Step [0]: Get the length of the list, which makes future calculations easy.
        n, dummy = 1, head
        while dummy.next: n, dummy = n+1, dummy.next

        # Store the last node for later.
        last = dummy 
        
        # Step [1]: Check base cases and adjust k as needed.  
        if n == 1: return head      # If the list is length 1, any rotation is the same.
        if k >= n: k = k % n        # Adjust k if >= len(list).
        if k == 0: return head      # If we rotate by 0, just return the list.
        
        # Step [2]: Find the critical nodes.
        # Critical nodes are the (k+1)th and kth node(s) from the back of the list.
        # The (k+1)th node from the back (n-k-1) should point to None, as it will be the new end node.
        # The kth node from the back (n-k) will be the node we return.
        i, dummy, knode, k1node = 0, head, None, None
        while i < n:
            if i == n - k - 1: k1node = dummy
            elif i == n - k: knode = dummy
            i, dummy = i + 1, dummy.next
        
        # Step [3]: Adjust all the relevant nodes:
        # a. The (k+1)th node should point to node.
        # b. The last node should now point to the head.
        # c. Return the kth node from the back.
        k1node.next = None
        last.next = head
        return knode
