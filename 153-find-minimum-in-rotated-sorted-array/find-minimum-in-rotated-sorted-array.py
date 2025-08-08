class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        # Use modified binary search to check the mid value against the right pointer
        # value and search the array accordingly: if value at mid > value at right pointer
        # search the right half otherwise search the left half until left ptr = right ptr
        while left_pointer != right_pointer:
            mid = (right_pointer + left_pointer) // 2
            if nums[mid] > nums[right_pointer]:
                left_pointer = mid + 1
            else:
                right_pointer = mid
            
        return nums[left_pointer]