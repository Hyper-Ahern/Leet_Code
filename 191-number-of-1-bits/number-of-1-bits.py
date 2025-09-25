class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        ones = 0

        # take the number, 'and' its least significant bit with 1 to check for 1's
        # then shit to the left and continue while counting the hamming weight (1's)
        # once there is no bits left, return the number of 1's as the answer.

        while n != 0:
            if (n & 1) == 1:
                ones += 1
            print (n)
            n >>= 1

        return ones