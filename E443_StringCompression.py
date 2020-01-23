# Example 1:
# Input:
# ["a","a","b","b","c","c","c"]

# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

# Example 2:
# Input:
# ["a"]

# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]

# Explanation:
# Nothing is replaced.
 

# Example 3:
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.

class Solution:
	def compress(self, chars):
		if chars == []:
			return 0
		if len(chars) == 1:
			return 
		n = len(chars)
		prev = chars[0]
		count = 1
		pos = 1 # position of current counter
		for e in enumerate(chars[1:]): # (0,a), (1,b) ...
			i, ch = e[0] + 1, e[1]
			if ch == prev:
				count += 1

				if i == n - 1: # last ch
					digits = list(str(count))
					chars[pos:pos+len(digits)] = digits
					pos += len(digits)

			else: # ch != prev
				if count > 1:
					digits = list(str(count)) # assign prev count
					chars[pos: pos + len(digits)] = digits
					pos += len(digits)

					chars[pos] = ch # followed with new ch
					pos += 1

				else: # count == 1
					chars[pos] = ch
					pos += 1

				count = 1
				prev = ch

		# after the for loop, pos = last counter position at the chars
		# we can safely remove the items after pos 
		chars = chars[:pos]
		print(chars)
		return len(chars)

		
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Solution().compress(chars)





