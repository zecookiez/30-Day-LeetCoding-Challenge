class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # Move all the non-zero elements to the front
        #     Use a pointer to indicate the next empty spot
        #     Fill the end with zeroes if there any any
        
        p1 = 0 # Pointer
        for val in nums:
            if val != 0: # Move item to the front
                nums[p1] = val
                p1 += 1  # Next empty spot is one spot after it.
        
        # Fill the end with the remaining zeroes
        for i in xrange(p1, len(nums)):
            nums[i] = 0
