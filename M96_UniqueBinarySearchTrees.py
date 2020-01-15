# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


# Brute force recursion: repeating subproblem calls 
# Idea: each value can be held as root
# [< root] root [>root]
# #Tree = #left * #right if root fix 

class Solution:
	
	def numTreesBF(self, n: int) -> int:
		if n <= 1:
			return 1
		if n == 2:
			return 2

		count = 0
		for i in range(1,n+1): # 1,2,3

			count += self.numTreesBF(i-1) * self.numTreesBF(n - i)
			# count += numTrees(0) * nt(2) = 2
			# count += numTrees(1) * nt(1) = 1 + 2 = 3
			# count += nt(2) * nt(1) = 2 + 3 = 5 
		# print(count)
		return count

	# Bottom up dynamic programming 
	# N[i] = numTree(i)
	# base case: N[0] = N[1] = 1, N[2] = 2
	# N[i] = N[k] * N[i-1-k] for k = 0 -> k = i - 1
	# idea: we can either place 0 node or i-1 nodes in left subtree
	def numTrees(self, n):
		N = [None for i in range(n+1)]
		N[0] = N[1] = 1
		return self.helper(n, N)

	def helper(self, n, N):
		if N[n] is not None:
			return N[n]

		for i in range(2, n+1):
			q = 0
			for k in range(0, i): #k = 0 -> i-1 on left subtree 
				q += self.helper(k, N) * self.helper(i-1-k, N) # place one as root 
			N[i] = q
		return N[n]

print(Solution().numTrees(3) == Solution().numTreesBF(3))