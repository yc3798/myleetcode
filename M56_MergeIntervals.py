# Overlap
# -----
#   ------

# --------
#  -----

# No overlaps
# -----
#        ------


# O(nlogn) solution
class Solution:
	def merge(self, intervals):

		if len(intervals) == 1:
			return intervals

		def comparator(t):
			return t[0]
    	
		ans = []
		# sort by lower bound in increasing order 
		intervals.sort(key = comparator)
		i = 0
		while i < len(intervals)-1: # len is changing 
			print(intervals[i], intervals[i+1])
			# case 1: merge to one at index i
			if intervals[i][1] >= intervals[i+1][0]: # overlap
				intervals[i] = [intervals[i][0],max(intervals[i][1],intervals[i+1][1])]
				intervals.pop(i+1)

			# case 2: no overlap, proceed
			else:
				i += 1
			print(intervals) 		





Solution().merge([[1,6],[2,4]])
Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]])