# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# sort each word, then group: O(n * mlogm) where m = max length of a string in strs
class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		if strs == []:
			return []
		group = {} # alpha combo: [indexes of anagram in strs]

		for i in range(len(strs)):
			# s is a str sorted in alpha order
			s = ''.join(sorted(strs[i]))
			if s in group:
				group[s].append(strs[i])
			else:
				group[s] = [strs[i]]
		ans = [group[key] for key in group.keys()]
		return ans