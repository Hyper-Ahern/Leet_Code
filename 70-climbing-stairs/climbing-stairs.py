class Solution:
    def climbStairs(self, n: int) -> int:

        # This turns into a fibbonaci sequence so I set up the base cases for 
        # dynamic programming here and made an array large enough
        ways = [0] * (n+1)
        ways[0] = 1
        ways[1] = 1

        # For every step, add the previous two steps to the current step as the
        # number of ways possible
        for i in range(2, n + 1):
            ways[i] = ways[i-1] + ways[i-2]

        # Return the last item in the list
        return ways[n]