class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp_index = len(s) - 1
        final_word_counter = 0
        final_word_index = 0

        # Working backwards from the end of the list to find the end of the last word
        while temp_index > 0:
            if s[temp_index] != ' ':
                final_word_index = temp_index
                temp_index = -1
            else:
                temp_index -= 1

        # Traversing the last word in reverse until it 'begins' with a space
        while s[final_word_index] != ' ' and final_word_index >= 0:
            final_word_counter += 1
            final_word_index -= 1

        return final_word_counter