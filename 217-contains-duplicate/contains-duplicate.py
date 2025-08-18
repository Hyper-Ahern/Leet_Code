class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        integer_set = set(nums)
        set_length = len(integer_set)
        list_length = len(nums)

        if list_length > set_length:
            return True
        else:
            return False