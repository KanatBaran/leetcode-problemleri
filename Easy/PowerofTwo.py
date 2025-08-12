class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        
        n1 = n - 1

        if (n & n1) == 0:
            return True
        else:
            return False