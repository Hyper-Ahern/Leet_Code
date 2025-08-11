class Solution(object):
    def twoSum(self, nums, target):
        # Doing it better than O(n^2)

        number_map = {}

        for index, number in enumerate(nums):
            complement = target - number
            
            if complement in number_map:
                return(number_map[complement], index)

            else:
                number_map[number] = index