class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) != 0:
            self.stack.append((x, min(self.stack[-1][1], x))) # Keep track of the minimum the same way as the stack
        else:
            self.stack.append((x, x))
        
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        assert len(self.stack) != 0
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        assert len(self.stack) != 0
        return self.stack[-1][1]
