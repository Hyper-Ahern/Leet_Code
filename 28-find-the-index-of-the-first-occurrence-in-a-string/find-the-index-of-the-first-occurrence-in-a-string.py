class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # left_pointer = 0
        # right_pointer = 0
        # haystack_length = len(haystack)
        # needle_length = len(needle)
        # index = -1
        # prefix_array = []
        # suffix_array = []

        # if needle_length > haystack_length:
        #     return index
        
        # while right_pointer < haystack_length:
        #     if haystack[left_pointer] == needle[]

        # Started to do it the manual way but realized that python has a built in
        # non-KMP time-optimized algorigth find function built in so...
        return haystack.find(needle)