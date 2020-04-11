/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    
    int diameter = 0;
    
    int diameterOfBinaryTree(TreeNode* root) {
        
        helper(root);
        
        return diameter;
        
    }
    
    int helper(TreeNode* node){
        
        if(node == NULL) return 0;
        
        // Get the longest path in both branches
        
        int LEFT  = helper(node->left);
        int RIGHT = helper(node->right);
        
        // Try to merge the two branches to form a diameter
        
        diameter = max(diameter, LEFT + RIGHT);
        
        return 1 + max(LEFT, RIGHT); // Add 1 to longest path
        
    }
    
};
