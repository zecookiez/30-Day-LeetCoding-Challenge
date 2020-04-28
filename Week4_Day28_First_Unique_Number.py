from collections import deque
class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        # O(1) Insertion
        # Amortized O(1) query, worst case is O(N)
        # Alternatively, you could use OrderedDict
         
        self.seen = set()
        self.dupe = set()
        self.unique = deque() # list of potential first unique numbers
        for val in nums:
            self.add(val)
            
    def showFirstUnique(self):
        """
        :rtype: int
        """
        # Remove the non-unique numbers until we reach a unique number
        # Since we remove once, we will only check O(N) times in total across all the queries
        while self.unique and self.unique[0] in self.dupe:
            self.unique.popleft()
        if not self.unique:
            return -1
        return self.unique[0]
    
    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value in self.seen:
            self.dupe.add(value)
        else:
            self.seen.add(value)
            self.unique.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
