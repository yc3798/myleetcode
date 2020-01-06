# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # BFS 
        if not root:
            return 0

        return self.BFS(root)
    
    def BFS(self, root):
        if not root:
            return 0
        elif not root.left and not root.right: # leaf node
            return 1       
        elif not root.left:
            return self.BFS(root.right) + 1
        elif not root.right:
            return self.BFS(root.left) + 1
        else: 
            return min(self.BFS(root.right), self.BFS(root.left)) + 1
            