class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        solution_index_1 = -1
        solution_index_2 = -1

        for index1, first_number in enumerate(nums):
                        
            for index2, second_number in enumerate(nums):

                if index1 == index2:
                    # Skip to the next iteration
                    pass

                elif (first_number + second_number == target):
                    #The solution is found; Print out the indices

                    solution_index_1 = index1
                    solution_index_2 = index2
                    
                    solution = [solution_index_1, solution_index_2]
                  
                    # solution = "[" + str(solution_index_1) + ", " + str(solution_index_2) + "]"
                    return(solution)

                else:
                    # Skip to the next iteration
                    pass


            

