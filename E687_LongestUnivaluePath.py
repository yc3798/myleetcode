# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Input:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output: 2


# Input:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 2

# Structure:
# 
# 1. left == root == right, return 2 + left + right 
# 2. left == root, return max(1 + left, right)
# 3. right == root, return max(1+right, left)
# 4. else: return max(right, left)

class Solution:
    
    # This helper function will return the longest chain length
    # that starts with the passing "node" that has the same vals with the passing "num"
    def helper(self, num, node):
              
        if not node: 
            return 0; # Return 0 if the node is NULL
        
        # Return 0 if the node has different val with the passing number
        # Meaning the chain is not connected after this point
        if node.val != num:
            return 0;
        
        # Get the results from its child nodes
        res_left = self.helper(node.val, node.left)
        res_right = self.helper(node.val, node.right)
        
        # Return the final result
        return 1 + max(res_left, res_right)
        
        
        
    def longestUnivaluePath(self, root: TreeNode) -> int:
        
        # Return 0 if the root is NULL   
        if not root:
            return 0;
        
        # Get the longest chain that passes through the root
        chain_through_root = self.helper(root.val, root.left)+self.helper(root.val, root.right)
        
        # Get the longest chain that doesn't pass through the root
        # 1. The chain that is from the left child
        chain_left_child = self.longestUnivaluePath(root.left)
        # 2. The chain that is from the right child
        chain_right_child = self.longestUnivaluePath(root.right)
        
        # Return the longest one
        return max(chain_through_root, chain_left_child, chain_right_child)