# Superstack implemented with list 
class Stack:
	def __init__(self):
		self.stack = []

	def push(self, x):
		"""push x to top"""
		self.stack.append(x)
		print(self.stack[-1])

	def pop(self):
		"""pop from top"""
		if self.stack != []:
			elem = self.stack.pop()

			if self.stack == []:
				print("EMPTY")
			else:
				print(self.stack[-1])

		else:
			print("EMPTY")

	def inc(self, pos, k):
		""" Add k to bottom pos elements in stack"""
		for i in range(pos):
			if i < len(self.stack):
				self.stack[i] += k
		print(self.stack[-1])

def superstack(ops):
	# parse the operations input 
	if ops == [] or ops == [0]: # no operations 
		return
	
	n = ops[0]
	# create stack
	mystack = Stack()

	def parse(op):
		command = op.split() 
		if command[0] == "push":
			mystack.push(int(command[1]))
		elif command[0] == "inc":
			mystack.inc(int(command[1]), int(command[2]))
		elif command[0] == "pop":
			mystack.pop()

	for i in range(1, n+1): # n operations in total
		parse(ops[i])

test = [12, "push 4", "pop", "push 3", "push 5", "push 2", "inc 3 1", "pop", "push 1", "inc 2 2", "push 4", "pop", "pop"]
superstack(test)