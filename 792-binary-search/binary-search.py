class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        list_size = len(nums)
        left_pointer = 0
        right_pointer = list_size - 1
        
        while (left_pointer <= right_pointer):
            middle = (right_pointer - left_pointer // 2)
            
            # Target is found, return index of target
            if nums[middle] == target:
                return middle

            # Target is less than middle element, therefore, use left side of array
            elif nums[middle] > target:
                right_pointer = middle - 1

            # Target is greater than middle element, therefore, use right side of array
            elif nums[middle] < target:
                left_pointer = middle + 1
                
        return -1
