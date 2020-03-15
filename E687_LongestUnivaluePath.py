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


# path has 3 form:
# 1. passing through root 
# 2. passing left node:
#    this case can further break into 3 cases: 
#    passing left node, passing left.left, passing left.right
# 3. passing right node
#    this case can further break into 3 cases: 
#    passing right node, passing right.right, passing right.right
# Structure: Define a helper to calculate longest path passing current node with identical val

# time: T(n) = T(k) + T(n-1-k) + n
# for simplicity assume balanced tree,
# time: T(n) = 2T(n/2)+ n
# O(nlogn)
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
        
        