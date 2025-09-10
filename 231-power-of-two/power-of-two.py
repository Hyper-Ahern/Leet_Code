class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # Base cases if n is 1 it's divisible by 2 else it is not
        if n == 1:
            return True
        elif n == 0:
            return False

        # If n % 2 is 0 it is an even number and an integer so floor division is
        # safe to use, otherwise it is not both and cannot be a multiple of 2
        if n % 2 == 0:
            return self.isPowerOfTwo(n//2)
        else:
            return False