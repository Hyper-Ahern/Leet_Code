# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # If there is nothing in head, there is no cycle, return False
        if not head:
            return False
        
        slow, fast = head, head

        # While fast and the fast.next node is ont null, move the pointers until they
        # either catch each other proving a cycle or they become null
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False