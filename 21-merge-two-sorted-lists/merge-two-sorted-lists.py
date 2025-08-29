# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # So I don't lose track of the head of the linked list as it is singly linked 
        # not doubly with no 'previous' function. Then I create a replica.
        dummy_node = ListNode()
        current = dummy_node

        # While there is a head for both list 1 and list 2, set the next node to the smaller
        # value, set the current node doing the work to the head of the list that lost the
        # item, and then set the head of the list itself to the next node in the linked list
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next

        # Once one of the lists points to null, set the next node to be the entire other list
        # because they are already sorted as input
        if list1:
            current.next = list1
        else:
            current.next = list2

        # The head of the linked list is found as the next node of the dummy_node
        return dummy_node.next