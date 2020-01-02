# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # build a reverse linked list and see if ll == revll
    def isPalindrome(self, head: ListNode) -> bool:
        # copy linkedlist 
        if head is None:
            return True
        
        headcopy = ListNode(head.val)
        prev = headcopy
        curr = head.next
        while curr is not None:
            prev.next = ListNode(curr.val)
            prev = prev.next
            curr = curr.next
        revhead = self.reverseLinkedList(headcopy)
        
            
        # if palindrome, revhead should be the same as original linkedlist 
        curr = head
        revcurr = revhead
        
        while curr is not None:
            if curr.val == revcurr.val:
                curr = curr.next
                revcurr = revcurr.next
            else:
                return False
        return True

    def reverseLinkedList(self,head) -> ListNode:
        curr = head
        prev = None
        nextNode = None
        
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

def reverseLinkedList(head): # modify in place 
	curr = head
	nextnode = None
	prev = None
	while curr is not None:
		nextnode = curr.next
		curr.next = prev
		prev = curr
		curr = nextnode
	return prev

def printLinkedList(node):
	while node:
		print(node.val)
		node = node.next

def buildLinkedList(lst):
	if lst == []:
		return None
	head = ListNode(lst[0])
	prev = head
	for i in range(1, len(lst)):
		curr = ListNode(lst[i])
		prev.next = curr
		prev = curr
	return head

l = [1,2,1,2,2,1]
head = buildLinkedList(l)
printLinkedList(head)
rev = reverseLinkedList(head)
printLinkedList(rev)
print(Solution().isPalindrome(head))