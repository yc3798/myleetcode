# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
#              Minimum cost: 2 + 5 + 3 = 10.

class Solution:
	def minCost(self, costs: List[List[int]]) -> int:
		if costs == []:
			return 0
		n = len(costs)
		sumcost = [[0, 0, 0] for i in range(n)]

		sumcost[0] = costs[0]

		for i in range(1, n):
			# choose Blue for i-th building
			sumcost[i][0] = costs[i][0] + min(sumcost[i-1][1], sumcost[i-1][2])
			# choose Green
			sumcost[i][1] = costs[i][1] + min(sumcost[i-1][0], sumcost[i-1][2])
			# choose Red
			sumcost[i][2] = costs[i][2] + min(sumcost[i-1][0], sumcost[i-1][1])
		# print(sumcost)
		return min(sumcost[n-1])