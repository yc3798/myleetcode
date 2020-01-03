# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]


# This is a Facebook interview question.
# They ask for the intersection, which has a trivial solution using a hash or a set.

# Then they ask you to solve it under these constraints:
# O(n) time and O(1) space (the resulting array of intersections is not taken into consideration).
# You are told the lists are sorted.

# Cases to take into consideration include:
# duplicates, negative values, single value lists, 0's, and empty list arguments.
# Other considerations might include
# sparse arrays.


class Solution:
	def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
		if nums1 == [] or nums2 == []:
			return []

		# sort O(logn + logm)
		nums1.sort()
		nums2.sort()

		i = 0
		j = 0
		intersection = set()
		while i < len(nums1) and j < len(nums2):
			if nums1[i] == nums2[j]:
				intersection.add(nums1[i])
				i += 1
				j += 1
			elif nums1[i] < nums2[j]:
				i += 1
			else:
				j += 1
		return intersection




