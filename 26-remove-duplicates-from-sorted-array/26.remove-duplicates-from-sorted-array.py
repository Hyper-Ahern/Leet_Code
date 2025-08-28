class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Got the original length, converted the list to a set then back again with underscores for
        # duplicates. This gives O(nlogn) instead of a two pointer approach for O(n)
        original_length = len(nums)
        number_set = set()
        number_set.update(nums)
        number_list = list(number_set) 
        final_length = len(number_set)

        # Sort the list
        number_list = sorted(number_list)
        
        # Added this before I realized the solution uses your K to slice the original nums list...
        # Very deceptive wording in this problem
        final_nums = ['_'] * original_length

        # Replace the original nums with the new unique list up until its length of unique numbers
        for i in range(final_length):
            nums[i] = number_list[i]
            
        return final_length