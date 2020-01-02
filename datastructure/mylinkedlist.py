# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printLinkedList(node):
	while node:
		print(node.val)
		node = node.next

def reverseLinkedList(head):
	curr = head
	nextnode = None
	prev = None
	while curr is not None:
		nextnode = curr.next
		curr.next = prev
		prev = curr
		curr = nextnode
	return prev

def buildLinkedList(lst):
	if lst == []:
		return None
	head = ListNode(lst[0])
	prev = head
	for i in range(1, len(lst)+1):
		curr = ListNode(lst[i])
		prev.next = curr
		prev = curr
	return head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d