# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

# Brute Force
import collections
class Solution:
	def leastInterval(self, tasks, n: int) -> int:
		# interval = 0, trivial 
		if n == 0:
			return len(tasks)

		# counttasks stores tasks:count
		counttasks = collections.Counter(tasks)

		# # sorted by count, rank = [A:3, B:2, C:2, D:1 ...]
		# rank = sorted(list(counttasks.items()), key = lambda i : i[1]) 
		# rank = []
		seq = []
		idle = "IDLE"

		while len(counttasks) > 0:
			for rank in range(n+1):
				if rank >= len(counttasks):
					seq.append(idle)  
				else:
					task = sorted(counttasks.most_common(rank + 1), key = lambda t: t[0])[-1][0]
					print(counttasks.most_common(rank + 1))
					counttasks[task] -= 1
					if counttasks[task] <= 0:
						del counttasks[task]
					seq.append(task)
				if len(counttasks) == 0:
					break


		print(seq)

Solution().leastInterval(["A","A","A","B","B","B"], 2)