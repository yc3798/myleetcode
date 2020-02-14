import heapq
import collectoions

# Brute force:
# sort, then use collections.Counter -> O(nlogn)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        count = collections.Counter(words)
        sortwords = list(count.keys())
        sortwords.sort(key = lambda w: (-count[w], w)) # reverse by count, then by word alphabetical 
        return sortwords[:k]


# IMPORTANT TECHNIQUE:
# TOP K:
# USE MINHEAP, HEAPIFY(key = -freq), POP LAST K!
# import heapq
# heapq.heappop, heapify

# better: O(nlogk)
# use a counter and a minheap (heapq)
# 1. counter O(n)
# 2. build heap using (word, -count) O(n)
#    keep smallest counts at top (heapify) O(logn)
# 3. pop last k items(O(klogk)) = O(nlogk) since k < n 


class Solution:
	def topKFrequent(self,words,k):
		count = collections.Counter(words) # O(n)
		# note when we create heap the key sequence matters 
		minheap = [(-freq, w) for w, freq in count.items()] # we want key be 1.-freq, 2.word alpha
		# heapify O(n)
		heapq.heapify(minheap)
		res = [heapq.heappop(minheap)[1] for i in range(k)]
		return res