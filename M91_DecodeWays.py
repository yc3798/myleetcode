class Solution:

	# DP: O(n) time and space
	# Count[i] = count[i-1] + count[i-2] if we can decode last digit, and last two digits
	def numDecodings(self, s: str) -> int:
		
		n = len(s)
		if n == 0:
			return 0


		# count[i] store decode ways for s[0...i]
		# base, i = 0, 1
		# 
		count = [None for i in range(n+1)]
		
		# initialize
		count[0] = 1
		count[1] = 0 if s[0] == "0" else 1

		for i in range(2, n + 1):
			pos = i - 1 # pos of i in s, for convenience
			curr = s[pos-1:pos+1] # last 2 digit
			res = 0
			# only when "10" <= curr <= "26" we need to include count[i - 2]
			# decode last two digits
			if curr >= "10" and curr <= "26":
				res += count[i - 2]

			# only when last single digit not 0, we can decode it
			if curr[-1] != "0":
				res += count[i - 1]
			count[i] = res
		return count[n]




	