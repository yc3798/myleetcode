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



# class Solution:
# 	def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:


a = makeLinkList([1,2,3,4,5])
reva = reverseLinkedList(a)
printLinkList(reva)