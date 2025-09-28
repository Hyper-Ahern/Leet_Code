class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Convert everything to a set, then make it into a list, reverse it, then sort it
        # because sets are inherently unordered, then find the 3rd or maximum element 
        # depending on the size of the list. This is not very efficient time-wise.

        num_set = set(nums)
        num_list = list(num_set)
        num_list = sorted(num_list)
        num_list = list(reversed(num_list))
        length = len(num_list)

        if length >= 3:
            answer = num_list[2]
        else:
            answer = num_list[0]

        return answer