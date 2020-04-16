class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # To efficiently keep track of the number of left parantheses you have right now, use two variables
        #     One is to track the maximum amount
        #     The other is to track the minimum amount
        #     Everything else will be in its range
        
        # Time complexity is O(N), memory complexity is O(1)
        
        left_low = left_high = 0
        for ch in s:
            if ch == "(":
                left_low  += 1
                left_high += 1
            elif ch == ")":
                left_low  = max(0, left_low - 1) # If left_low was 0, then we turn one of the previous * into an empty char
                left_high -= 1
                if left_high < 0: # Even when maximized we don't have enough left brackets
                    return False
            else:
                left_low  = max(0, left_low - 1) # Turn * into empty char if left_low == 0
                left_high += 1 # Maximize left brackets
        
        return left_low == 0
