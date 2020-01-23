# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# Example 1:

# Input: "3+2*2"
# Output: 7
# Example 2:

# Input: " 3/2 "
# Output: 1
# Example 3:

# Input: " 3+5 / 2 "
# Output: 5

# O(n) memory and time
# using list
class Solution:
    def calculate(self, s: str) -> int:
        # remove white spaces
        s = s.replace(" ", "")
        # if s is num return
        if s.isnumeric():
            return int(s)

        def findNextNum(i:int) -> (int, int):
            """Return next number and index of next operator"""
            num = 0
            i += 1 # i is operator
            while i < len(s) and s[i] not in "+-*/":
                num = num * 10 + int(s[i])
                i += 1
            return num, i

        # current number and next operator
        curr, i = findNextNum(-1)
        stack = [curr]
        # insert all numbers into stack
        while i < len(s):
            curr, next_i = findNextNum(i)
            if s[i] == "+":
                stack.append(curr)
            elif s[i] == "-":
                stack.append(-curr)
            elif s[i] == "*":
                stack[-1] *= curr
            else: # "/"
                if stack[-1] >= 0:
                    stack[-1] = stack[-1] // curr
                else: # negative case cannot directly apply //
                    stack[-1] = -((-stack[-1])//curr)
            i = next_i
        return sum(stack)
        
                


# stack
class Solution:
    def nextNum(self, s, i):

    def calculate(self, s: str) -> int:
        # remove white spaces
        s = s.replace(" ", "")
        # if s is num return
        if s.isnumeric():
            return int(s)

        num_stack = []
        ops_stack = []

        # find the last +/- operator, else first * / /
        n = len(s)
        pos = None

        for i in range(n-1, -1, -1):
            # mult, div have higher priority
            if s[i] == "+" or s[i]== "-":
                pos = i
                break
            if s[i] == "*" or s[i] == "/":
                pos = i

        left = s[:pos]
        right = s[pos + 1:]

        if not right.isnumeric() and not left.isnumeric():
            num_stack.insert(0, self.calculate(right))
            num_stack.insert(0, self.calculate(left))


        elif not right.isnumeric():
            num_stack.insert(0, self.calculate(right))
            num_stack.insert(0, int(left))

        elif not left.isnumeric():
            num_stack.insert(0, int(right))
            num_stack.insert(0, self.calculate(left))        

        else: 
            num_stack.insert(0, int(right))
            num_stack.insert(0, int(left))

        ops_stack.insert(0, s[pos])

        while ops_stack != []:
            op = ops_stack.pop(0)
            if op == "+":
                res = num_stack.pop(0) + num_stack.pop(0)
            elif op == "-":
                res = num_stack.pop(0) - num_stack.pop(0)
            elif op == "*":
                res = num_stack.pop(0) * num_stack.pop(0) 
            else: # op == "/"
                res = num_stack.pop(0) // num_stack.pop(0) 

            num_stack.insert(0, res)
        # print(num_stack)
        return num_stack[0]
    
s = "3-2*2"
Solution().calculate(s)
# # minus
# s = " 5 - 2 "
# Solution().calculate(s)
# s = " 5 / 2 + 4"
# Solution().calculate(s)
# s = " 1 + 5 / 2 + 4"
# Solution().calculate(s)
# s = " 1 + 5 / 2 + 4 * 2 + 1"
# Solution().calculate(s)
# s = "2-3+4"
# Solution().calculate(s)