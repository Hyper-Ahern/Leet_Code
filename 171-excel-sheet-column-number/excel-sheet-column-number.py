class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0

        # We are working in a base 26 system where AB is 26 * 1 + 26 * 0 + 2 or 28 and
        # we math with ascii as 64 to make A(ascii 65) into '1'

        for char in columnTitle:
            result = result * 26 + (ord(char) - 64)

        return result