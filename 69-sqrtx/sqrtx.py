class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        square_root = 0
        left_pointer = 0
        right_pointer = x
        middle = 0

        while left_pointer <= right_pointer:
            middle = (right_pointer + left_pointer) // 2

            if (middle * middle == x):
                return middle
            
            elif (middle * middle > x):
                right_pointer = middle - 1
            
            elif (middle * middle < x):
                square_root = max(square_root, middle)
                left_pointer = middle + 1
                
        return square_root