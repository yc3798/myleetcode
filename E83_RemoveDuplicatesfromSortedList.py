# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Example 1:

# Input: 1->1->2
# Output: 1->2
# Example 2:

# Input: 1->1->2->3->3
# Output: 1->2->3

# Iterate once. Track prev, if curr.val == prev.val, remove curr(prev -> curr.next).
# O(n) time and O(1) space

class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		if not head:
			return None

		curr = head 
		prev = None

		while curr:
			if prev and prev.val == curr.val:
				prev.next = curr.next
				curr = curr.next

			else:
				prev = curr
				curr = curr.next
		return head



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
	if len(lst) == 1:
		return head
	prev = head
	for i in range(1, len(lst)):
		curr = ListNode(lst[i])
		prev.next = curr
		prev = curr
	return head

##### Testing 
# 1. dup
dup = [1,2,3,3,4,5,5] 
head = buildLinkedList(dup)
nodup = Solution().deleteDuplicates(head)
printLinkedList(nodup)
# 2. no dup
dup = [1,2,3] 
head = buildLinkedList(dup)
nodup = Solution().deleteDuplicates(head)
printLinkedList(nodup)
# 3. all dup
dup = [1,1,1] 
head = buildLinkedList(dup)
nodup = Solution().deleteDuplicates(head)
printLinkedList(nodup)
# 4. single element
dup = [1] 
head = buildLinkedList(dup)
nodup = Solution().deleteDuplicates(head)
printLinkedList(nodup)
