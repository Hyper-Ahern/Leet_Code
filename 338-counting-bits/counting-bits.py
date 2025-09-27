class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        answer = []

        # This is the brute force approach. For each number up to n, iterate through
        # that numbers bits and grab the hamming weight (number of 1's). Add that to
        # the dynamic array as the ith entry

        for i in range(n+1):
            count = 0
            number = i
            while number != 0:
                if (number & 1) == 1:
                    count += 1
                number >>= 1

            answer.append(count)

        return answer