# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursively examine if leftnode.left == rightnode.right AND leftnode.right == rightnode.left
class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:
		# empty tree
		if not root:
			return True
		return self.isReverse(root.left, root.right)

	def isReverse(self, r1, r2):
		if not r1 and not r2:
			return True
		elif not r1 or not r2 or r1.val != r2.val:
			return False
		else:
			return self.isReverse(r1.right, r2.left) and self.isReverse(r1.left, r2.right)