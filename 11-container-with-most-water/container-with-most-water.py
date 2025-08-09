class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Initialize varibles and pointers
        left_pointer = 0
        right_pointer = len(height) - 1
        max_water = 0

        # while the two pointers are on their respective sides, take minimum of the leftmost and 
        # rightmost heights, multiply them by the difference between the two heights (essentially the
        # size of what the curent container would be) and take that as the amount of water this 
        # container would hold. Always take the max of that and previous maximums
        while left_pointer <= right_pointer:
            left_height = height[left_pointer]
            right_height = height[right_pointer]
            container_diff = right_pointer - left_pointer
            water = container_diff * (min(left_height, right_height))
            max_water = max(water, max_water)

            # Move the smallest of the heights inward until the pointers meet
            if left_height < right_height:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water