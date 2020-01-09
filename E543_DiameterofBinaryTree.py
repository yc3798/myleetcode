# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # include root: left + right + 1 
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxfromleft = self.diameterOfBinaryTree(root.left)
        maxfromright = self.diameterOfBinaryTree(root.right)
        maxfromroot = 2 + self.pathlength(root.left) + self.pathlength(root.right)
        return max(maxfromleft, maxfromright, maxfromroot)
    
    def pathlength(self, root): # single path length
        if not root:
            return -1
        return max(self.pathlength(root.left), self.pathlength(root.right)) + 1