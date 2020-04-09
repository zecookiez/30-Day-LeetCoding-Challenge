class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        # O(N) time and O(1) memory solution
        # Why we need to parse the two strings in revserse:
        #     Visualize the #s as closing parantheses
        #         If we parse the string forwards, we need some sort of way to track the characters (especially due to repeating #s). That becomes impossible with constant memory.
        # 
        # How do we parse this in reverse?
        #     Keep track of the number of #s you encounter
        #         "Delete" the character by shifting backwords
        #         Return the next valid position
        
        # This problem is misleading -- The straightforward solution will have better memory complexity in real life situations
        # If you need to save the user keystrokes into a string, you are already using O(N) memory.
        
        # On the other hand, reading it from front to back allows you to process the operations in realtime -- this is known as online querying
        # In practical situations the straightforward array solution should not even require an input string.
        
        p1 = self.get_char(S, len(S) - 1)
        p2 = self.get_char(T, len(T) - 1)
        while p1 >= 0 <= p2:
            if S[p1] != T[p2]:
                return False
            p1 = self.get_char(S, p1 - 1)
            p2 = self.get_char(T, p2 - 1)
        return p1 == -1 == p2
    
    def get_char(self, inp, pos):
        deleted = 0
        while pos >= 0:
            if inp[pos] == "#":
                deleted += 1
            elif deleted != 0:
                deleted -= 1
            else:
                return pos
            pos -= 1
        return -1
