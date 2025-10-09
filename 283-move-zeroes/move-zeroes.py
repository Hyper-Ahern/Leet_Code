class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # If there is a 0 at index i, skip it. When a non-zero element comes up, swap it to the
        # place where 'non_zero' is, then update that variable by one. We are essentially 
        # shifting all non-zero elements to the front of the list which will leave the 0's at
        # the end but instead of the very front, its the last known non_zero location.
        
        non_zero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1