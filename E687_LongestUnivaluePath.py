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
    
    def helper(self, val, node):
        """
        Return the longest path passing current node and 
        all values equals val (node's parent val)
        """
        if not node or node.val != val:
            return 0
        return max(self.helper(val, node.left), self.helper(val, node.right)) + 1

    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0 

        maxfromroot = self.helper(root.val, root.left) + self.helper(root.val, root.right)
        maxfromleft = self.longestUnivaluePath(root.left)
        maxfromright = self.longestUnivaluePath(root.right)

        return max(maxfromroot, maxfromleft, maxfromright)
        
        