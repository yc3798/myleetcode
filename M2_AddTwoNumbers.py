# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    
    # === SOL 1: NON-REC ===    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # brute force 
        hd = l1
        acc = 0
        repeat = True
        
        while repeat:
            l1.val = l1.val + l2.val + acc 
            acc = 0 # reset
            
            # handle val > 9
            if l1.val > 9:
                acc = 1 
                l1.val -= 10
            
            if not l1.next and not l2.next:
                if acc == 0:
                    repeat = False
                else:
                    l1.next = ListNode(0)
                    l2.next = ListNode(0) 
                    
            elif not l1.next:
                l1.next = ListNode(0)
            elif not l2.next:
                l2.next = ListNode(0)   
            
            l1 = l1.next
            l2 = l2.next
            
        return hd
    
    # === SOL 2: TRY REC === 
