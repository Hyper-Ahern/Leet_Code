class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Strip everything away from the string leaving all lowercase alphanumerics
        phrase = []

        for char in s:
            if char.isalnum():
                phrase.append(char)

        phrase = "".join(phrase)
        phrase = phrase.lower()

        left_pointer = 0
        right_pointer = (len(phrase) - 1)

        # Traverse the list from left and right evaluating character equivalency at each
        # step. If the check fails, it is not a palindrome
        while left_pointer <= right_pointer:
            if phrase[left_pointer] != phrase[right_pointer]:
                return False
            else:
                left_pointer += 1
                right_pointer -= 1
                
        return True