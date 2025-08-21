class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # # Brute Force Approach that IS correct and functional but times-out on one test case

        # max_profit = 0
        
        # for i in range(len(prices)):

        #     # Iterate over the list backwards starting at the end and stopping BEFORE i
        #     for j in range (len(prices) - 1, i, -1):
        #         if (prices[j] - prices[i]) > max_profit:
        #             max_profit = prices[j] - prices[i]

        # return max_profit


        # Two Pointer Solution to reduce time complexity to O(n) from o(n^2) above

        left_pointer = 0
        right_pointer = 1
        max_profit = 0

        while right_pointer <len(prices):

            if prices[left_pointer] < prices[right_pointer]:
                max_profit = max(max_profit, (prices[right_pointer] - prices[left_pointer]))
                right_pointer += 1

            else:
                left_pointer = right_pointer
                right_pointer += 1


        return max_profit
