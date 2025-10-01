class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        # Because only positive numebrs can be ugly, anything under 0 is not ugly.
        # Keep dividing by 2, 3, and 5 until either a 1 remains which means it
        # only has those as factors and is ugly, or it isn't 1 in which case it
        # has another factor that isn't 2, 3, or 5 and is therefore not ugly.

        if n <= 0:
            return False

        while n % 2 == 0:
            n = n / 2

        while n % 3 == 0:
            n = n / 3

        while n % 5 == 0:
            n = n / 5

        if n == 1:
            return True
        else:
            return False