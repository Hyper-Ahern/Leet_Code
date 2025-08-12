# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # Define Variables for use
        first_number = []
        second_number = []
        retrieved_list_1 = []
        retrieved_list_2 = []

        # Iterate over the linked list and retrieve the contents
        current_node = l1
        while current_node is not None:
            retrieved_list_1.append(current_node.val)
            current_node = current_node.next

        current_node = l2
        while current_node is not None:
            retrieved_list_2.append(current_node.val)
            current_node = current_node.next

        # Reverse the lists (could have done it manually by creating another list and iterating)
        retrieved_list_1.reverse()
        retrieved_list_2.reverse()

        # Add the numbers together (Used the mathematical conversions because there are no leading zeroes to worry about)
        number1_to_add = 0
        number2_to_add = 0

        for number in retrieved_list_1:
            number1_to_add = number1_to_add * 10 + number

        for number in retrieved_list_2:
            number2_to_add = number2_to_add * 10 + number

        added_number_integer = number1_to_add + number2_to_add

        # Create a new array with the reveresed number in it (used the string conversion)
        
        added_number_array = list(map(int, str(added_number_integer)))
        added_number_array.reverse()

        # Create a new linked list and place the newly added and reversed number in it
        final_linked_list = ListNode()
        temp = final_linked_list

        for number in added_number_array:
            temp.next = ListNode(number)
            temp = temp.next
            
        return final_linked_list.next