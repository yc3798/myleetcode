# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 

# hash table, linear runtime
class Solution:
	def singleNumber(self, nums) -> int:
		d = {}
		for i in nums:
			if i in d:
				d[i] += 1
			else:
				d[i] = 1
		for i in d.items():
			if i[1] == 1:
				return i[0]

input1 = [2,2,1]
input2 = [4,1,2,1,2]
Solution().singleNumber(input1)
Solution().singleNumber(input2)
