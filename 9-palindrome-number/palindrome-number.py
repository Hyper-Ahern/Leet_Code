class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        left_pointer = 0
        number_as_string = str(x)
        number_length = len(number_as_string)
        right_pointer = number_length - 1

        while left_pointer < right_pointer:

            if number_as_string[left_pointer] != number_as_string[right_pointer]:
                return False

            left_pointer += 1
            right_pointer -= 1
            
        return True