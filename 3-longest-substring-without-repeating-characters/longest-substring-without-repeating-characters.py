class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Initilazing varibles
        final_int = 0
        string_length = len(s)
        window = set()
        left_pointer = 0
        right_pointer = 0

        # Checking for strings of size 0
        if not s:
            return final_int

        # Intiating the sliding window
        for i in range(string_length):

            while s[right_pointer] in window:
                window.remove(s[left_pointer])
                left_pointer += 1
                
            window.add(s[right_pointer])
            right_pointer += 1

            # Update the final return integer or rather the largest substring length
            if final_int < (right_pointer - left_pointer):
                final_int = (right_pointer - left_pointer)
            else:
                pass

        return final_int