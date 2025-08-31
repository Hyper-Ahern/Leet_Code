class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        subtraction_counter = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 101
                subtraction_counter += 1

        nums.sort()
        
        return len(nums) - subtraction_counter