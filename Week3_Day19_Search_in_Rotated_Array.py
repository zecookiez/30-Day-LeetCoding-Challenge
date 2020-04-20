class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # O(log n) time complexity
        
        from bisect import bisect_left as search
        
        if len(nums) == 0:
            return -1
        
        # Binary search to find the peak
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = left + right >> 1
            if nums[mid] < nums[left]: # Is not it monotonic?
                right = mid
            else:
                left = mid
        
        # The peak splits the array into two halves that are strictly increasing
        # Binary search individually in both halves
        
        low_half  = search(nums, target, lo = right)
        high_half = search(nums, target, hi = right)
        
        if low_half < len(nums) and nums[low_half] == target:
            return low_half
        elif nums[high_half] == target:
            return high_half
        
        return -1
