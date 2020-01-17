

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true


# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false


# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false


class Solution:
	def isAlienSorted(self, words, order: str) -> bool:
		# Create a dictionary with char:index given order: O(len(order))
		n = len(words)
		d = {order[i]:i for i in range(len(order))}
		d[''] = -1 # empty string has lowest rank
		for i in range(1,n):
			if not self.helper(words[i-1], words[i], d):
				return False
		return True

	# a recursive helper: return True if w1 <= w2
	def helper(self, w1, w2, d):
		print("comparing: ", w1, w2)
		if w1 == w2 or w1 == '':
			return True
		if w2 == '' or d[w1[0]] > d[w2[0]]: # w1 != '', w2 == '', w2 < w1 must hold, return False
			return False
		if d[w1[0]] < d[w2[0]]:
			return True
		return self.helper(w1[1:], w2[1:], d)


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
Solution().isAlienSorted(words,order)
words =["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
Solution().isAlienSorted(words,order)
words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
Solution().isAlienSorted(words,order)