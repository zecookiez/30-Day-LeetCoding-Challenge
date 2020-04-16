class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # To do this without division:
        #     Keep prefix product and suffix product.
        #     We can combine the prefix and suffix:
        #         Arr: [1,   2,  3,  4]
        #         Pre: [1,   2,  6, 24]
        #         Suf: [24, 24, 12,  4]
        #         Output[2] will be Pre[1] * Suf[3]
        
        # To do this in constant memory (excluding output array):
        #     Creating prefix and suffix arrays is impossible
        #     The next best thing is to modify the input array itself and the output array
        
        # Default product is 1
        
        output = [1 for i in nums]
        
        # Prefix
        
        for i in xrange(1, len(output)):
            output[i] *= output[i - 1] * nums[i - 1]
        
        # Suffix
        
        for i in xrange(len(output) - 2, -1, -1):
            nums[i] *= nums[i + 1]
            output[i] *= nums[i + 1]
        
        return output
        
        
