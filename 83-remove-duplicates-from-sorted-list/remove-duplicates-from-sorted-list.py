# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        current = dummy_node

        # For edge cases of 1 or null input
        if not head:
            return
        elif not head.next:
            return head

        # While head isn't null, check the current value and the next value, if they are the
        # same, set head to head.next and try again until they aren't
        while head:
            if head.next:
                if head.val == head.next.val:
                    head = head.next
                    print('if')
                else:
                    current.next = head
                    current = head
                    head = head.next
                    print('else')
            else:
                current.next = head
                break

        return dummy_node.next