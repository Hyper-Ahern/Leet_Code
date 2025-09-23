class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Sort the array, get the number that is 1 index further than half which
        # according to the problem is guarenteed to exist, return it as the answer

        nums.sort()
        return nums[len(nums) // 2]