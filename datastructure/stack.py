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
	def parse(command):
		if command[0] == "p"