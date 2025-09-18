# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        result = head
        length = 1

        # if there is no head, return itself (null)
        if not head:
            return head

        # Count the length of the linked list
        while head.next:
            length += 1
            head = head.next

        # if the length and n are the same, you are deleting the only node so return Null
        if length == 1 and n == 1:
            return None
        
        # Reset head pointer to the original and caluclate which node needs to be deleted which
        # tells us how many iterations we need to get to the node before it
        head = result
        to_delete =  length - n - 1

        # if the node to delete is less tahn the length of the list, it means the first
        # node needs to be deleted and so we return head.next as the start of the list
        if to_delete < 0:
            return head.next

        # Get to the node BEFORE the one needed to be deleted because this is a singly list
        for i in range(to_delete):
            head = head.next

        # if after all this, n is 1 and we arrived at the node in question, return null,
        # because we are eliminating from the END of the list, otherwise set the node we 
        # are at next node to be the one after it which eliminates the node we are trying to get rid of
        if n == 1:
            head.next = None
        else:
            head.next = head.next.next
            
        return result