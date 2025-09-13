# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = None

        # If head is null, return it
        if not head:
            return dummy_node

        # While head is not null, make a temp variable, swap the current node to point
        # to the previous, then move the new list forward until head is null
        while head:
            temp = head.next
            head.next = dummy_node
            dummy_node = head
            head = temp
        
        return dummy_node