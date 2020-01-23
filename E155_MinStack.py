# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack


# 1. Implemented with list: [(val, currMin)]
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] # [(val, currMin)]
        

    def push(self, x: int) -> None:
        if self.stack == []:
            self.stack.append((x,x))
        else:
            currMin = self.stack[-1][1]
            self.stack.append((x, min(currMin, x)))

    def pop(self) -> None:
        return self.stack.pop(-1)[0]
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack == []:
            return None
        else:
            return self.stack[-1][1]
        

# 2. Singly Linked List, with a link to currMin node
# each time we push/pop at head 

class MyNode:
    def __init__(self, x, nextNode = None, currMin = None):
        self.val = x
        self.nextNode = nextNode
        self.currMin = currMin

class MinStack:
    def __init__(self):
        """ Initialize linked list . """
        self.head = None

    def push(self, x):
        """ Push to top of stack"""
        if self.head == None:
            self.head = MyNode(x, None, x)
        else:
            # push to head of linkedlist
            currMin = min(x, self.head.currMin)
            newHead = MyNode(x, self.head, currMin)
            self.head = newHead

    def pop(self):
        """ pop from top of stack """

        # head of linked list
        if self.head is None:
            return None
        else:
            curr = self.head.val
            self.head = self.head.nextNode
            return curr

    def top(self):
        """ return top """ 
        if self.head is None:
            return None
        return self.head.val

    def getMin(self):
        """ return min value """
        if self.head == None:
            return None
        else:
            return self.head.currMin

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()