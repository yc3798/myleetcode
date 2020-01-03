# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:

# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14

import math

class Solution:
	def checkPerfectNumber(self, num: int) -> bool:
		if num <= 0:
			return False
		i = 1
		sum_num = num
		while sum_num >= 1 and i <= num/2 + 1:
			if num % i == 0:
				sum_num -= i
				print(i)
			i += 1
		return sum_num == 0

	def better(self, num):
		if num <= 1:
			return False
		sum_num = 1
		i = 2 
		while i <= math.sqrt(num):
			if num % i == 0:

				if i**2 != num: 
					sum_num = sum_num + i + num/i
				else:
					sum_num += i
			i += 1

		return sum_num == num

print("28:", Solution().checkPerfectNumber(28))
print("1:", Solution().checkPerfectNumber(1))
print("28:", Solution().better(28))
print("1:", Solution().better(1))
