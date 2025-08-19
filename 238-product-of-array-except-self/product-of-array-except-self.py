class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Initializaing Varibales
        array_length = len(nums)
        prefix_array = [1]*array_length
        suffix_array = [1]*array_length
        prefix = 1
        suffix = 1
        solution = [1]*array_length

        # Creating a Prefix Product Array
        for i in range(array_length):
            prefix_array[i] = prefix
            prefix *= nums[i]

        # Creating a Suffix (or Postfix) Product Array
        for i in range(array_length - 1, -1, -1):
            suffix *= nums[i]
            suffix_array[i] = suffix

        # Merging the prefix and suffix arrays to get the Product Array Except Self
        for i in range(array_length):
            if i == array_length-1:
                solution[i] = prefix_array[array_length-1]

            else:
                solution[i] = prefix_array[i] * suffix_array[i+1]

        return solution