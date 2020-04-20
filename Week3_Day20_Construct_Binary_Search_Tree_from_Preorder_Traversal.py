# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        
        # Do a depth-first search on the nodes, O(N) time complexity
        
        def helper(pos, midpoint = float("Inf")):
            
            # End condition of a branch (out of bounds or belongs to the right side)
            if pos >= len(preorder) or preorder[pos] > midpoint:
                return None, pos
            
            # Create root
            root = TreeNode(preorder[pos])
            
            # Explore left side
            root.left, pos = helper(pos + 1, preorder[pos])
            
            # Explore right side
            root.right, pos = helper(pos, midpoint)
            
            return root, pos
        
        return helper(0)[0]
