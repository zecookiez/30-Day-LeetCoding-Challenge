class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Approach 1: set()
		#   This will work in the general case, but memory complexity will become O(N)
		#   Although set operations in Python are O(1), the slowdown will become visible after 10^6 items as there is a little bit of overhead.
		
		# Approach 2: Bit manipulation with XOR
        
        # X ^ X == 0, all the items that appear twice become 0
        # 0 ^ 0 == 0, in the end, we are left with 0 if every item appears twice
        # X ^ 0 == X, the item that appears once is the odd one out
        
        dup = 0
        for val in nums:
            dup ^= val
        return dup
