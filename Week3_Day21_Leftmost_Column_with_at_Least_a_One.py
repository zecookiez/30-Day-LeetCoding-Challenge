# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        
        """
        # O(N log M) solution (92ms, 13.1mb)
        n, m = binaryMatrix.dimensions()
        left = -1
        right = m
        while right - left > 1:
            mid = left + right >> 1
            if any(binaryMatrix.get(i, mid) for i in xrange(n)):
                right = mid
            else:
                left = mid
        if right == m:
            return -1
        return right
        """
        
        # O(N + M) solution (92ms, 13.1mb)
        n, m = binaryMatrix.dimensions()
        
        # Walk down from the top right corner
        # If you find a one -> Move to the left
        
        y = m - 1
        for x in xrange(n):
            while y >= 0 and binaryMatrix.get(x, y) == 1:
                y -= 1
        if y == m - 1:
            return -1
        return y + 1
