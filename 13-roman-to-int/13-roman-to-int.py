class Solution:
    def romanToInt(self, s: str) -> int:
        # Declare and initialize variables and value dictionaries
        final_number = 0
        conversion_dictionary = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        skip_letter = False

        for letter in range(len(s) - 1, -1, -1):            
            # Becuase this input string seems implemented as a circular array, 
            # add the number 'first' number if the iterator is at the 'end' of the list
            if letter == 0 and not skip_letter:
                final_number += (conversion_dictionary[s[letter]])
                continue

            # If there was a subtraction pair last iteration, reset the skip_letter
            # because it was already added to the total
            if skip_letter:
                skip_letter = False
                continue
           
            # If the currently letter isn't one of the known subtraction cases, add to the total amount,
            # if not, subtract from current letter, skip the next iteration, and add to the total amount
            if s[letter - 1] == 'I' and (s[letter] == 'V' or s[letter] == 'X') and not skip_letter:
                final_number += (conversion_dictionary[s[letter]] - 1)
                skip_letter = True
            elif s[letter - 1] == 'X' and (s[letter] == 'L' or s[letter] == 'C') and not skip_letter:
                final_number += (conversion_dictionary[s[letter]] - 10)
                skip_letter = True
            elif s[letter - 1] == 'C' and (s[letter] == 'D' or s[letter] == 'M') and not skip_letter:
                final_number += (conversion_dictionary[s[letter]] - 100)
                skip_letter = True
            else:
                final_number += (conversion_dictionary[s[letter]])
                
        return final_number