# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        
        # ngl the problem title was very annoying to put into a file name
        
        # O(N), where N is the number of nodes
        
        def helper(depth, node):
            if node.val != arr[depth]: # Doesn't match
                return False
            if depth + 1 == len(arr): # Fully matched
                return node.left == None == node.right # Check if node is a leaf
            if node.left and helper(depth + 1, node.left): # Explore left side
                return True
            return node.right and helper(depth + 1, node.right) # Explore right side
        return helper(0, root)
