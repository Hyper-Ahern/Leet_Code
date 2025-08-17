class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
       # Initlizaing variables and sorting the list alphabetically
        longest_prefix =""
        sorted_list = strs
        strs.sort()
        first_word_length = len(sorted_list[0])

        # If there is no length, an empty string, or a string with one word
        if not len(strs):
            return longest_prefix

        if len(strs) == 1:
            return sorted_list[0]

        if not sorted_list[0]:
            return longest_prefix

        # Iterate through the first and last word and compare individual characters
        for i in range (len(sorted_list[0])):
            if first_word_length == 0:
                return longest_prefix

            if sorted_list[0][i] == sorted_list[len(sorted_list) - 1][i]:
                longest_prefix += sorted_list[0][i]
                first_word_length -= 1
            else:
                return longest_prefix

        return longest_prefix