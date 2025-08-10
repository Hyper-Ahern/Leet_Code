class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Setting the max_sum to a number lower than the test cases allows
        max_sum = -1000000
        current = 0

        # If there is 1 number in the list, return it
        if len(nums) <= 1:
            max_sum = nums[0]

        # If the current sum is less than 0, it will never increase without a positive number
        # so set it to 0 if so, then take the max of the running total and the previous max_sum
        for number in nums:
            if current < 0:
                current = 0

            current += number
            max_sum = max(max_sum, current)

        return max_sum