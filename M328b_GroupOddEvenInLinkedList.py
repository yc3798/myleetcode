# 画图，分case处理，记录prev_odd:最近发现的odd node; prev; curr
# 每次找到odd node时，将其提出insert after previous odd node prev_odd，
# 注意处理提出时的prev, next以及insert处的prev, next。
# 如果prev_odd还没找到时insert into head
# update prev_odd, prev, curr （note that prev does not need update if we take out curr)# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# case: 
# 1. all even, no change 
# 2. all odd, no change
# 3. mixed 
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# 

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
    if len(lst) == 1:
        return head
    prev = head
    for i in range(1, len(lst)):
        curr = ListNode(lst[i])
        prev.next = curr
        prev = curr
    return head

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        curr = head
        prev_odd = None
        prev = None
        index = 1
        # In the first iteration we only re-organize the nodes(focus on value instead of index)
        while curr:
            if curr.val % 2 != 0: # odd, set prev_odd
                if not prev: # we are at head
                    # curr.val = index
                    prev = curr
                    prev_odd = curr
                    curr = curr.next

                elif prev and not prev_odd: 
                    # this is the first odd we find,
                    #take out curr and insert at head
                    # curr.val = index
                    tempnext = curr.next
                    prev.next = tempnext
                    curr.next = head
                    head = curr
                    curr = prev.next
                    prev_odd = head
                    # prev does not change
                    
                elif prev == prev_odd: # prev is also odd
                    # curr.val = index
                    prev_odd = curr
                    prev = curr
                    curr = curr.next
                else: # prev is even, we take out curr and insert it after prev_odd
                    # curr.val = index
                    tempnext = curr.next
                    prev.next = tempnext
                    prevnext = prev_odd.next
                    prev_odd.next = curr
                    curr.next = prevnext
                    prev_odd = curr # update prev_odd 
                    curr = tempnext
                    # prev does not change
                    
            else: # even value: continue on
                # curr.val = index
                prev = curr
                curr = curr.next

            index += 1
        return head

a = buildLinkedList([1,2,2,1,2,2,2,1])

b = Solution().oddEvenList(a)
printLinkedList(b)