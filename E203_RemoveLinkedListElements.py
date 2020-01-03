# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def removeElements(self, head: ListNode, val: int) -> ListNode:
		if head is None:
			return head

		prev = None
		curr = head

		while curr is not None:
			if curr.val == val:
				# curr is head
				if not prev:
					head = curr.next

				# curr is tail
				elif curr.next is None:
					prev.next = None
					prev = curr

				# curr has prev and next
				else:
					prev.next = curr.next
			else:
				prev = curr
			
			curr = curr.next
		return head 