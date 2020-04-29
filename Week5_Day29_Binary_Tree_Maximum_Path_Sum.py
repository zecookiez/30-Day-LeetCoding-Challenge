# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            best = max_p = node.val
            l_path = -1e18
            if node.left: # Explore left path
                best1, l_path = helper(node.left)
                max_p = max(max_p, l_path + node.val) # Furthest path down the left side
                best  = max(best, best1, max_p)       # Overall longest path
            if node.right:
                best2, r_path = helper(node.right)    
                max_p = max(max_p, r_path + node.val) # Furthest path down the right side
                best  = max(best, best2, node.val + r_path + max(l_path, 0)) # Overall longest path
            return best, max_p
        return helper(root)[0]
