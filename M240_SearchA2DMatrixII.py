
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:

# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]

# Given target = 5, return true.

# Given target = 20, return false.

# BFS search
class Solution:
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if matrix == []:
			return False
		m = len(matrix)
		n = len(matrix[0]) # m x n matrix

		# keep track of BFS visit
		visited = {(i,j): False for i in range(m) for j in range(n)}

		def BFS(i,j):
			# go either right or down
			if i < 0 or j < 0 or i == m or j == n or visited[(i,j)]:
				return False
			visited[(i, j)] = True
			if matrix[i][j] == target:
				return True
			return BFS(i + 1, j) or BFS(i, j + 1) 

		return BFS(0, 0)

