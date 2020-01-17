# 1/16
# 560. Subarray Sum Equals K
# Given an array of integers and an integer k, 
# you need to find the total number of continuous subarrays whose sum equals to k.

# Input:nums = [1,1,1], k = 2
# Output: 2


# 1. Dynamic Programming: O(n^2)
# S[i,j] = sum of subarray nums[i...j]
# base case: S[i,i] = nums[i]
# S[i,j] = S[i, j-1] + nums[j]
# we only need to fill upper triangular part of S matrix

# Edge case:
# 记得数本身nums[i] == k


# 2. Use HashMap to store {sum:count} O(n)
# Each step, check if (sum - k) in d AND if sum == k
# Reasoning: [....i....j], if sum[j] - sum[i] = k, subarray found. 
# so we need to count how many times a sum has occured when we iterate through the array


# recall subset sum: if array contains subset with sum equals k 
# This is different case!!

class Solution:
	# 2. Hashmap O(n)
	def subarraySum(self,nums, k):
		n = len(nums)
		S = [0 for i in range(n)]
		d = {}
		count = 0
		for i in range(n):
			S[i] = S[i-1] + nums[i] # S[i] stores sum of array nums[...i]
			# check if S == k 
			if S[i] == k:
				count += 1
			if S[i] - k in d:
				count += d[S[i] - k]

			if S[i] in d:
				d[S[i]] += 1
			else:
				d[S[i]] = 1
		return count

			
	# 1.
	def subarraySumDP(self, nums:List[int], k : int) -> int:
		n = len(nums)

		# edge cases
		if n == 0:
			return 1 if k == 0 else 0
		if n == 1:
			return 1 if nums[0] == k else 0

		S = [[0 for j in range(n)] for i in range(n)]

		count = 0

		# Initialize 
		for i in range(n):
			S[i][i] = nums[i]
			if S[i][i] == k:
				count += 1

		for i in range(n):
			for j in range(i + 1,n):
				S[i][j] = S[i][j-1] + nums[j]
				if S[i][j] == k:
					count += 1
		return count