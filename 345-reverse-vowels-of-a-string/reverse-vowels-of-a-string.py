class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Turn the string into a list so it can be modified. Use two pointers to 
        # find where vowels occur on either end and swap them until the pointers meet 
        # in the middle. Then when the whole list is iterated and swapped, cast it to 
        # a string and return it.

        left_ptr = 0
        right_ptr = len(s) - 1
        vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        s = list(s)

        while left_ptr < right_ptr:
            if s[left_ptr] not in vowel_set and left_ptr != right_ptr:
                left_ptr += 1
            
            if s[right_ptr] not in vowel_set and left_ptr != right_ptr:
                right_ptr -= 1

            if s[left_ptr] in vowel_set and s[right_ptr] in vowel_set:
                temp = s[left_ptr]
                s[left_ptr] = s[right_ptr]
                s[right_ptr] = temp
                left_ptr += 1
                right_ptr -= 1

        return "".join(s)