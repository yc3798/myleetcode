# 1/15 


class Solution:
# Note: naive approach to perfrom DFS from rightmost branch was wrong! 
# Need to consider case when left branch has greater depth!!!

	# def rightSideView(self, root) -> List[int]:
	# 	if root:
	# 		return self.helper(root, [])
	# 	return []

	# def helper(self, root, lst):
	# 	# reach the leaf
	# 	if not root.left and not root.right:
	# 		return lst + [root.val]
	# 	if root.right:
	# 		return self.helper(root.right, lst + [root.val])
	# 	else:
	# 		return self.helper(root.left, lst + [root.val])



	# Perform BFS, record rightmost item at each level
	# stored in prevval
	# we know we reach rightmost node(prevval) when level changes
	# O(n) time and space 
	def rightSideView(self,root):
		if not root:
			return []
		queue = [(root, 0)]
		ans = []
		prevdepth = 0
		# record previous node value,
		# when we reach a new depth, this value store the rightmost value of last depth
		prevval = root.val
		while queue != []:
			node, depth = queue.pop(0)
			if depth > prevdepth:
				ans.append(prevval)
				prevdepth = depth
			if node:
				queue.extend([(node.left, depth + 1), (node.right, depth + 1)])
				prevval = node.val
		return ans