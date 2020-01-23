# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
import math

class Solution:
	def spiralOrder(self, matrix):
		if matrix == [] or matrix == [[]]:
			return []

		# boundary 
		upper = -1
		lower = len(matrix)
		left = -1
		right = len(matrix[0])
		ans = []

		move = {"up":(-1, 0), "down": (1, 0), "left":(0, -1), "right":(0, 1)} # direction change
		nextmove = {"up":"right", "right":"down", "down":"left", "left":"up"} # next possible dir given current dir 

		def visit(i,j,d,upper, lower, left, right):

			if (i >= lower or i <= upper) and (j >= right or j <= left):#  or upper >= lower and left >= right:
				ans.append(matrix[i][j])
				# print(i,j,upper, lower, left, right)
				return

			# calculate next pos following current direction
			next_i = i + move[d][0]
			next_j = j + move[d][1]

			# adjust bounds and next direction if we reach a boundary

			if next_i <= upper: # reach upper bound, turn right, narrow down left bound 
				return visit(i,j, nextmove[d], upper, lower, left + 1, right)

			if next_i >= lower: # reach lower bound, turn left, narrow down right bound 
				return visit(i,j, nextmove[d], upper, lower, left, right - 1)

			if next_j <= left: # narrow down lower bound
				return visit(i,j, nextmove[d], upper, lower - 1, left, right)

			if next_j >= right:
				return visit(i,j, nextmove[d], upper + 1, lower, left, right)

			# visit current cell
			ans.append(matrix[i][j])

			return visit(next_i,next_j, d ,upper, lower, left, right)
		
		visit(0,0,"right",upper,lower,left,right)
		# print(ans)
		return ans


m = [[1,2,3],[4,5,6],[7,8,9]]
Solution().spiralOrder(m)

