class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        # 'A' uppercase English letter is ascii code 65 so this helps map the alphabet
        adjust_ascii = 65

        # To map the entire English alphabet in upper case
        counter = [0] * 26

        left_pointer = 0
        s_length = len(s)

        for right_pointer in range(s_length):

            # Add the character currently looked at into the approriate bucket in the counter array
            # by subtracting the adjust_ascii (65) from the ascii value of the current character
            counter[ord(s[right_pointer]) - adjust_ascii] += 1

            # Set the window length and the maximum number of characters in the alphabet counter
            window_length = (right_pointer - left_pointer) + 1
            max_counter = max(counter)

            # (Window length - max of counter) > K means the window is invalid so we must shrink the
            # window from the left towards the right until there are only K changes in the substring
            while (right_pointer - left_pointer + 1) - max(counter) > k:
                counter[ord(s[left_pointer]) - adjust_ascii] -= 1
                left_pointer +=1

                # Reset the variables for the loop to include new calculations
                window_length = (right_pointer - left_pointer) + 1
                max_counter = max(counter)

            result = max(result, window_length)

        return result