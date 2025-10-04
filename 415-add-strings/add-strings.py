class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        length1 = len(num1)
        length2 = len(num2)
        number1 = 0
        number2 = 0

        # Did it both ways to showcase the ability to condense the math code. Take the string
        # version of the number, subtract the ord of '0' from it (48) to get the integer as an
        # int. Then multiply that number by the magnitude (digit place) which is added to the
        # cumulative result. Finally, add them together and make them into a string again.

        for i in range(length1):
            number1 += (ord(num1[i]) - ord('0')) * (10 ** ((length1 - i) - 1))

        for i in range(length2):
            number = ord(num2[i]) - ord('0')
            magnitude = (length2 - i) - 1
            magnitude = 10 ** magnitude
            number = number * magnitude
            number2 += number
        
        result = number1 + number2
        return str(result)