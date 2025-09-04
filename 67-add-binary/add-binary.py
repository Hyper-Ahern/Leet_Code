class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # This way b is always the smaller string: Easier to work with
        if len(a) < len(b):
            a, b = b, a
        
        # Initiallizing variabled and adding leading zeroes to the smallest string for ease
        carry = 0
        added_array = []
        length_a = len(a)
        length_b = len(b)
        length_diff = length_a - length_b
        
        for i in range(length_diff):
            b = '0' + b

        # Adding together from right to left and recording the carry
        for i in range(len(b) - 1, -1, -1):
            temp = int(a[i]) + int(b[i])
            if temp == 0 and carry == 0:
                added_array.insert(0, 0)
            elif temp == 0 and carry == 1:
                added_array.insert(0, 1)
                carry = 0
            elif temp == 1 and carry == 0:
                added_array.insert(0, 1)
            elif temp == 1 and carry == 1:
                added_array.insert(0, 0)
                carry = 1
            elif temp == 2 and carry == 0:
                added_array.insert(0, 0)
                carry = 1
            elif temp == 2 and carry == 1:
                added_array.insert(0, 1)
                carry = 1

        # If there is a carry left over, add it to the start of the list
        if carry == 1:
            added_array.insert(0, 1)

        # Turn the array of ints into a single string and return it
        final_string = "".join(str(item) for item in added_array)
        return final_string