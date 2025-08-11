class Solution(object):
    def twoSum(self, nums, target):

        for index1, first_number in enumerate(nums):
                        
            for index2, second_number in enumerate(nums):

                if index1 == index2:
                    # Skip to the next iteration
                    pass

                elif (first_number + second_number == target):
                    #The solution is found; Print out the indices

                    return [index1, index2]  
