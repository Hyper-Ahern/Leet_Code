class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            mid = (right_pointer + left_pointer) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left_pointer = mid + 1
            elif nums[mid] > target:
                right_pointer = mid - 1
                
        return left_pointer