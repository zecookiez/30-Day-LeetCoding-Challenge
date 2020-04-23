class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # Initial solution -> Loop through all bit positions
        #    Check if a bit is entirely set in the range:
        #    A bit is set IFF:
        #        m and n's bits are both set (Start and end with the ith bit set)
        #        n - m does not exceed 2^ith bit (Make sure it does not turn to 0 partway through the range)
        
        # 60ms submission
        #ans = 0
        #for i in xrange(0, 32):
        #    # Check if all numbers in [m, n] have ith bit set
        #    if m & (1 << i) and n & (1 << i) and (n - m) < (1 << i):
        #        ans |= 1 << i
        #return ans
        
        # We can optimize this!
        # The only bits that will matter are when n and m's bits are both set
        #     There is a fast way to loop through the set bits of (n & m)
        # This one runs in 32ms :)
        
        mask = n & m
        lim = n - m
        while mask:
            lsb = mask & -mask # (n - m) < (1 << i), mask & -mask grabs the LSB of mask
            if lim < lsb:
                return mask # as the LSB increases, every set bit afterwards will be set as well
            mask ^= lsb # clear the LSB
        return 0 
