class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        
        # We can calculate the final offset without simulatin but by treating it as integers
        
        offset = 0
        for direction, qnt in shift:
            if direction == 0:
                offset -= qnt
            else:
                offset += qnt
                
        # The result may be negative or may be more than the length of the string itself.
        # Performing modulo will cut it down
        offset %= len(s)
        
        # Python string slicing
        return s[-offset:] + s[:-offset]
