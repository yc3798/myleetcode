
# stack: LIFO, so can only push to top/move from  
# Queue: FIFO 

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.q.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.q == []:
            return None

        dq = self.q[0]
        self.q = self.q[1:]
        return dq

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.q == []:
            return None
        return self.q[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.q == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# MyQueue queue = new MyQueue();

# queue.push(1);
# queue.push(2);  
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false