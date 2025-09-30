class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # Make a set of already seen numbers, enter a loop, if the same number comes up
        # we are stuck in a loop and therefore its not a happy number. If we exit the
        # loop it means that n = 1 which makes it a happy number so return true. 

        seen = set()

        while n != 1:
            if n in seen:  
                return False

            seen.add(n)
            result = 0

            while n > 0:
                remain = n % 10
                result += remain * remain
                n = n // 10
            n = result

        return True