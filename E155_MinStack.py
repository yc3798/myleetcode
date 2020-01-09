class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min = None # index of min
        self.minvalue = None
        self.len = 0

    def push(self, x: int) -> None:
    	self.len += 1
        if s == []:
        	self.min = 0
        	self.minvalue = x
        elif x < self.minvalue:
        	self.minvalue = x
        	self.min = self.len - 1
        s.append(x)


    def pop(self) -> None:
        self.s.remove(self.len - 1)
    	if self.len - 1 == self.min:
    		self.updateMin()
        self.len -= 1

    def top(self) -> int:
        return self.s[self.len - 1]

    def getMin(self) -> int:
    
    def updateMin(self):
    	self.min = min(self.s)
    	self.minvalue = 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()