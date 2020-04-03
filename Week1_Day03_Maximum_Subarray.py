class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # O(N) memory solution (more intuitive)
        # Dynamic Programming
        
        #DP = [-1e18] * (len(nums) + 1)
        #for pos, i in enumerate(nums):
        #    DP[pos] = max(DP[pos - 1] + i, i) # Best current answer, or reset it entirely.
        #return max(DP)
        
        # O(1) memory solution (excluding the input)
        
        cur = 0
        best = max(nums) # No empty-subarrays! Our trivial case is the highest number in the array
        for i in nums:
            cur = max(i, cur + i) # Two options: Use the previous subarray + i, or use i by itself.
            if cur > best: # Update the highest subarray
                best = cur
        return best
