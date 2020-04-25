class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import OrderedDict
        
        # OrderedDict was made for this, although I am not quite sure if the removal of an item is truly O(1)
        
        self.container = OrderedDict()
        self.limit = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.container:
            return -1
        val = self.container[key] = self.container.pop(key)
        return val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.container:
            self.container.pop(key)
        elif len(self.container) == self.limit:
                self.container.popitem(last=0)
        self.container[key] = value
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
