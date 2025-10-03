class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        output = [0] * n 

        # Test each number from 1 to n for divisibility by 3, 5, or 3 & 5 then replace 
        # the premade array at that index with the words if divisibility is true. If not,
        # replace the index with a string cast of that int so the array is all strings.

        for i in range(1, n + 1):

            if i % 3 == 0 and i % 5 == 0:
                output[i - 1] = 'FizzBuzz'
            elif i % 3 == 0:
                output[i - 1] = 'Fizz'
            elif i % 5 == 0:
                output[i - 1] = 'Buzz'
            else:
                output[i - 1] = str(i)
        
        return output