class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

def printLinkList(node):
	while node: 
		print(node.val)
		node = node.next

def makeLinkList(lst):
	head = ListNode(lst[0])
	curr = None
	prev = head
	for i in range(1,len(lst)):
		curr = ListNode(lst[i])
		prev.next = curr
		prev = curr
	return head

def reverseLinkedList(head): 
	prev = None
	curr = head 
	while curr:
		temp = curr.next
		if prev:
			curr.next = prev
		if not prev:
			# head 
			curr.next = None
		prev = curr
		curr = temp
	return prev 
 

class Solution:
	def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
		# 1->2->3
		# 2->4
		# res: 1->4->7
		# recursion? 
		# if next, 

		if not l1.next and not l2.next:
			# add
			val = l1.val + l2.val
			prev = ListNode(0)
			if val >= 10:
				val -= 10
				prev = ListNode(1)
			prev.next = ListNode(val)
			return prev
		elif not l1.next: 

			self.addTwoNumbers(l1, l2.next)





a = makeLinkList([1,2,3,4,5])
reva = reverseLinkedList(a)
printLinkList(reva)