# 1/15
# Naive BFS
# Use BFS(FIFO queue), track depth and a visit order index along the traversal. - O(n) 
# record d = {depth:[first non-None index, ...,last non-None index]}
# return max diff from d - O(depth)
# since the greatest depth is O(n), runtime is O(n)
# space: O(depth)

# when do we stop the BFS:
# when in d we have d[depth - 1] = []
class Solution:
	def widthOfBinaryTreeBF(self, root: TreeNode) -> int:
		if not root:
			return 0
		curr = [] # current level non-None node indexes(BFS visit sequence)
		index = 0
		queue = [(root, 0)]
		maxwidth = 0
		prev_depth = 0
		while queue != []:
			node, depth = queue.pop(0)
			# proceeding to next level
			if depth > prev_depth:
				# if last level is all None, break the loop
				if curr == []:
					break
				maxwidth = max(curr[-1] - curr[0] + 1, maxwidth)
				curr = []
				prev_depth = depth

			if not node is None:
				queue.extend([(node.left, depth + 1),(node.right, depth + 1)])
				curr.append(index)

			else:
				queue.extend([(None, depth + 1), (None, depth + 1)])
			# print(curr)
			index += 1
			prev_depth = depth
		
		return maxwidth


# Smart BFS: 不需要append None Node，直接计算出non-None node的position用于计算每个level的width，
# 仍然需要track when we reach next level 
# width at each level = pos - left + 1
	def widthOfBinaryTree(self, root: TreeNode) -> int:
		if not root:
			return 0
		queue = [(root,0,0)] # node, depth, pos index
		prevdepth = 0
		depth = 0
		maxwidth = 0
		left = 0 # left most index at current depth
		while queue != []:
			node, depth, pos = queue.pop(0)
			# We only care about index of Non-None node
			if node: 
				# if we reach next level in BFS search, update prev_depth, left 
				if depth > prevdepth:
					left = pos
					prevdepth = depth
				maxwidth = max(maxwidth, pos - left + 1)
				queue.append((node.left, depth + 1, pos * 2 + 1))
				queue.append((node.right, depth + 1, pos * 2 + 2))
		return maxwidth





