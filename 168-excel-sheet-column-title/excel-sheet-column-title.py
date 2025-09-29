class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        answer = []
        i = columnNumber

        # (701-1) % 26 is 24 which in string.ascii_uppercase is Y. We append that,
        # and then change 701 to 700 // 26 which is 26. Repeat for Z to append that.
        # We are shaving down any given column number to represent and append its 
        # ascii representation.
        
        while i > 0:
            answer.append(string.ascii_uppercase[(i - 1) % 26])
            i = (i - 1) // 26

        return "".join(reversed(answer))