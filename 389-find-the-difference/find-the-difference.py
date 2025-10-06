class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # Sort both lists and iterate through until one doesn't match. If they all match,
        # then the last element of t must be the added letter

        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]

        return t[len(t) - 1 ]