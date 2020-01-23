# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
# For example, there won't be input like 3a or 2[4].


# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


# recursion 
# s = #[...]..., return 3 * decode(...) + decodeString(...)
class Solution:
	def decodeString(self,s):
		# print("processing ", s)
		if s == "" or s.isalpha():
			return s

		nstart = nend = None # index of first number 
		left = right = 0 
		start = end = None # index of first set of []

		# look for the first code [..]
		for i in range(len(s)):
			if nstart is None and s[i].isnumeric():
				nstart = i
				nend = i + 1
			elif nstart is not None and s[nstart:i + 1].isnumeric():
				nend = i + 1

			elif s[i] == "[":
				if left == 0:
					start = i
				left += 1
			elif s[i] == "]":
				if right + 1 == left:
					end = i
					break
				right += 1
		
		code = s[start + 1 : end] # "[...]"
		mult = int(s[nstart:nend])
		ans = s[:nstart] + mult * self.decodeString(code) + self.decodeString(s[end + 1:])
		# print(ans)
		return ans

# tests:
s = "3[a]2[b]"
Solution().decodeString(s)
s = "3[a2[c]]"
Solution().decodeString(s)
s = "3[a2[cb4[d]]]"
Solution().decodeString(s)

