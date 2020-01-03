
# Definition for a Node.
class Node:
    def __init__(self, x: int, next, random):
        self.val = int(x)
        self.next = next
        self.random = random


# Naive approach: use a hashmap to store each Node, 
# iterate twice, assign random at the 2nd iteration
class Solution:
	def copyRandomList(self, head):
		if not head:
			return None
		cphead = None
		cpcurr = None
		cpprev = None
		curr = head

		A = {}  # oldnode : newnode
		while curr:
			cpcurr = Node(curr.val, None, None)
        	
			if not cphead:
				cphead = cpcurr
	
			if cpprev:
				cpprev.next = cpcurr
			A[curr] = cpcurr 
			cpprev = cpcurr
			curr = curr.next

		# iterate again to assign random
		curr = head
		while curr:
			if curr.random:
				A[curr].random = A[curr.random]
			curr = curr.next
		return cphead



