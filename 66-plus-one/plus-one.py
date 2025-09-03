class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_length = len(digits)
        num_as_int = 0
        magnitude = 1

        # Ran through the loop backwards changing the list to an int
        for i in range(digits_length - 1, -1, -1):      
            num_as_int += (digits[i] * magnitude)
            magnitude = magnitude * 10
        
        # Found the length of the int and initialized the final array
        num_as_int += 1
        int_length = len(str(num_as_int))
        final_num_array = [0] * int_length
        mod_magnitude = 10
        div_magnitude = 1

        # Ran through the list backwards and used mod + division math to
        # isolate the current unit looked at and add it to the final array
        for i in range(int_length - 1, -1, -1):
            
            temp_num = num_as_int % mod_magnitude
            final_num_array[i] = temp_num // div_magnitude
            div_magnitude = div_magnitude * 10
            mod_magnitude = mod_magnitude * 10
        
        return final_num_array
            
