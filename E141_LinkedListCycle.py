# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.


# Mark "visited" nodes, O(n) time and O(1) space complexity 
# Idea similar to hash table  
import sys
class Solution:
    def hasCycle(self, head) -> bool:
        if head is None:
            return False # empty LL has no cycle 
        
        curr = head
        while curr:
            if curr.val == sys.maxsize:
                return True
            # mark visited node
            curr.val = sys.maxsize
            curr = curr.next
        return False

    # using set
	def hasCycleHT(self, head):
		if head is None:
			return False
		visited = set()
		curr = head
		while curr:
			if curr in visited:
				return True
			visited.add(curr)
			curr = curr.next 
		return False