# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findmin(self,v):
        """find min from binary tree"""
        if v.left is None and v.right is None:
            return v.val
        elif v.left is None:
            return min(self.findmin(v.right),v.val)
        elif v.right is None:
            return min(self.findmin(v.left),v.val)
        else:
            return min(self.findmin(v.left),self.findmin(v.right),v.val)
            
    def findmax(self,v):
        """find max from binary tree"""
        if v.left is None and v.right is None:
            return v.val
        elif v.left is None:
            return max(self.findmax(v.right),v.val)
        elif v.right is None:
            return max(self.findmax(v.left),v.val)
        else:
            return max(self.findmax(v.left),self.findmax(v.right),v.val)
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is not None and self.findmax(root.left) >= root.val:
            return False
        if root.right is not None and self.findmin(root.right) <= root.val:
            return False
        if (self.isValidBST(root.left) == False or self.isValidBST(root.right) == False):
            return False
        return True
    
