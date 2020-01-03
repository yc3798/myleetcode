# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Naive approach: make lists and then find intersection by iterating lists from back to front 
# Time: O(m+n), space:O(m+n)
# TODO: TRY TWO POINTERS 
class Solution:
	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
		if not headA or not headB:
			return None

		A = []
		B = []

		curr = headA
		while curr:
			A.append(curr)
			curr = curr.next

		curr = headB
		while curr:
			B.append(curr)
			curr = curr.next

		n = len(A) - 1
		m = len(B) - 1

		while n >= 0 and m >= 0:
			if A[n] == A[m]:
				n -= 1
				m -= 1
			else:
				break
		if n < len(A) - 1:
			return A[n+1]

		return None