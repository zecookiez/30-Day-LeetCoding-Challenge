class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        # With O(N) memory, we can use a hashmap/dictionary to count the occurences of every element.
        
        # O(N log N) solution, O(1) memory
        # 12ms on Leetcode in Python2.7
        
        total = prev = prevInc = 0
        for num in sorted(arr, reverse = True):
            if num != prev:
                prev, prevInc = i, prev - 1
            if num == prevInc:
                total += 1
        return total
