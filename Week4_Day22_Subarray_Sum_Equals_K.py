class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # Let's get the prefix sum array
        # 
        #    The sum of a subarray is now equivalent to PSA[right] - PSA[left - 1]
        #    
        #    PSA[right] - PSA[left - 1] = K
        #    PSA[right] = K + PSA[left - 1]
        #
        #    We now must count the number of PSA items that satisfy this. Using a dictionary will suffice
        
        hmap = {k: 1}
        tsum = tot = 0
        for i in nums:
            tsum += i
            if tsum in hmap:      # Add the number of items that satisfy the equation
                tot += hmap[tsum]
            if tsum + k in hmap:  # Insert PSA[left - 1] + K
                hmap[tsum + k] += 1
            else:
                hmap[tsum + k] = 1
        return tot
