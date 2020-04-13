class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Let's reduce this to a prefix sum array problem:
        # If we replace the 0s into -1s, the problem changes to finding subarrays with a sum of 0.
        #     In other words: PSA[right] - PSA[left] = 0
        #                     PSA[right] == PSA[left]
        #
        # If we get the prefix sum array, the longest subarray are the two duplicates that are the furthest apart
        # This can be solved using a dictionary/hashmap.
        #
        # Time complexity: O(N)
        # Memory complexity: O(N)
        
        csum = longest = 0
        hmap = {0: -1}
        for j, i in enumerate(nums):
            csum += i or -1
            if csum not in hmap: # Assign the leftmost index
                hmap[csum] = j
            else: # Found a subarray
                longest = max(longest, j - hmap[csum])
        return longest
