# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        head = root
        self.helper(head)
        
    def helper(self, node):
        if not node.left and not node.right: # leaf node
            print("1", node.val)
            return node
        elif not node.left: # flatten right subtree
            print("2", node.val)
            return self.helper(node.right)
        elif not node.right:
            print("3", node.val)
            # move left node to right and flatten right subtree
            node.right = node.left
            node.left = None
            return self.helper(node.right)
        else: # both left and right nodes exist
            print("4", node.val)
            temp = node.right
            # move left part to right and flatten this part first
            node.right = node.left
            node.left = None
            nextnode = self.helper(node.right)
            nextnode.right = temp
            return self.helper(nextnode.right)



