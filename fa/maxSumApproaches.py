def maxSubArray(A): #O(n)
	n = len(A)
	if n == 0:
		return -1,-1
	globalmax = -10000 # -Inf 
	curr = nums[0] # first element
	for i in range(1, n):
		# idea: if sum [... , i] < i, restart curr from i and update globalmax
		curr = max(nums[i], curr + nums[i])
		globalmax = max(globalmax, curr)
	return globalmax 

def maxSubBF(A): # O(n^2)
	n = len(A)

	maxsum = 0 # -Inf 
	for i in range(len(A)):
		curr = 0 
		for j in range(i,n):
			curr = curr + A[j]
			maxsum = max(maxsum, curr)
	print(maxsum)


def maxSubArrayDP(A): #O(n) dynamic programming
	n = len(A)
	if n == 0:
		return 0
	m = [0 for i in range(n)]
	m[0] = A[0] 
	maxsum = A[0]
	for i in range(1,n):
		m[i] = max(A[i], m[i-1]+A[i])
		maxsum = max(m[i], maxsum)
	print(m)
	return(m)
	# print("max in m :",maxsum)

def maxSubArrayDP2(A): #O(n) dynamic programming
	n = len(A)
	if n == 0:
		return 0
	m = [0 for i in range(n)]
	m[0] = A[0]
	current = A[0] 
	for i in range(1,n):
		# print(A[i], current)
		# idea: m[i] save maxSubarray from A[0] to A[i]
		current = max(current+A[i], A[i])
		m[i] = max(m[i-1],current)

	print(m)
	return(m)
	# print("max in m :",max(m)) 
	# return(m)

def printM(m):
	n = len(m)
	if n == 0:
		return(None, None)
	maxsum = max(m)
	k = n-1
	j = None 
	while k != -1:
		if m[k] == maxsum:
			j = k
		if j is not None and m[k] <= 0:
			break
		k = k - 1
	i = k + 1
	print(i, j) 

def topK(A, k):
	n = len(A)
	m = [[-100 for j in range(k)] for i in range(n)]
	m[0][0] = A[0]
	for i in range(1,n):
		val = A[i]
		larger_i = False
		# print(m[i])
		for j in range(k):
			if val > m[i-1][j] and not larger_i: 
				m[i][j] = val 
				largeri = True
			elif largeri:
				m[i][j] = m[i-1][j-1]
			else:
				m[i][j] = m[i-1][j]

			# 	val = m[i-1][j]
			# else:
			# 	m[i][j] = m[i-1][j]
	print(m)

# def pickNonAdjacent(A,n):
# 	m = [None for i in range(n)]
# 	# if n == 1:
# 	# 	return A[0]
# 	# if n == 2:
# 	# 	return max(A[0],A[1])
# 	return pickNonAdjHelper(A,n,m)

M = [0 for i in range(12)]
# def NonAdjMaxSum(A,n):
# 	M = [None for i in range(n)] 
#   return helper(A, n, M)

	
# def helper(A,n,M):
# 	maxsum = 0
# 	if M[n] is not None:
# 		return M[n] # already computed
# 	if n == 0:
# 		maxsum = A[0]
# 	elif n == 1:
# 		maxsum = max(A[0],A[1])
# 	else:
# 		maxsum = max(A[n] + helper(A, n-2, M), helper(A,n-1, M))
# 	M[n] = maxsum
# 	return M[n]

def pickNonAdj(A,n):
	print("...")
	maxsum = 0
	if M[n] != None:
		return M[n]
	
	if n == 0:
		maxsum = A[0]
	
	elif n == 1:
		maxsum = max(A[0],A[1])
	else:
		maxsum = max(A[n] + pickNonAdj(A, n-2), pickNonAdj(A,n-1))
	M[n] = maxsum
	print(M)
	return M[n]

B = [None for i in range(10)] 
B[:2] = [0, 1]
def SmartFib(n):
	if B[n] is not None:
		return B[n]
	B[n] = SmartFib(n-1) + SmartFib(n-2)
	print(B)
	return B[n]

def SuperSmartFib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	fib = 0
	prev1 = 0
	prev2 = 1
	i = 2
	while i <= n:
		fib = prev1 + prev2
		prev1 = prev2 
		prev2 = fib 
		i+=1
		print(fib)
	return fib


C = [None for i in range(10)]
C[0] = 1
C[1] = 1
def AllPossibleBST(n):
	if C[n] is not None:
		return C[n]
	count = 0
	for i in range(1,n+1):
		count += AllPossibleBST(i-1) * AllPossibleBST(n-i)
	C[n] = count 
	print(C)
	return C[n]
AllPossibleBST(3)


SuperSmartFib(5)
SmartFib(5)



a1 = [-2,1,-3,4,-1,2,1,-5,4,10,7,-2] # 6 

# topK(a1,3)

a2 = [-1,3,-2,1] # 3
pickNonAdj(a1,11)
# a3 = [-1,-2,-8] 
# a4 = [10,-2,4,-8] 
# a5 = [-1,10,-2,4,-8,100]
# a6 = [-1, 2, -5, 3, 14, 7, -10, 0, -3]
# tests = [a1, a2,a3,a4,a5,a6]
# for a in tests:
# 	print("A = ", a)
# 	# maxSubBF(a)
# 	maxSubArrayDP(a)
# 	printM(maxSubArrayDP(a))
# 	# maxSubArrayDP2(a)
