# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False
        elif s.val == t.val:
            return (self.isEqual(s.left, t.left) and self.isEqual(s.right, t.right)) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isEqual(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None or s.val != t.val:
            return False
        return self.isEqual(s.left, t.left) and self.isEqual(s.right, t.right)
