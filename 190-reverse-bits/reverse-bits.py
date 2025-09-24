class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """

        # shift the result to the left, add the least significant bit each time 
        # to the result from the input and then shift the input to the right. The
        # and is to make sure the bit is reversed when added to the result

        result = 0

        for i in range(32):
            result = result << 1       
            result += (n & 1)       
            n = n >> 1    

        return result