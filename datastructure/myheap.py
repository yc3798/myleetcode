def poscount(A, i, n):
	if i >= n: 
		return 0 
	if A[i] <= 0:
		return 0 
	left = poscount(A,2*i+1,n)
	right = poscount(A,2*i+2,n)
	pos = left+right+1
	return pos 

def kposcount(A, i, n, k):
	if k == 0:
		return 0
	if i >= n: 
		return 0 
	if A[i] <= 0:
		return 0 
	print(i,A[i],k)

	left = kposcount(A,2*i+1,n,k-1)
	k = k - left
	if k > 0:
		right = kposcount(A,2*i+1,n,k-1)
		
	return left + right + 1


hp1 = [0] # return 0
hp2 = [0,0,0]
hp3 = [10,7,9,-1,-2,3,6] # return 5 
hp4 = [10, 0,-1] # return 1
hp5 = [10,2,5,-2,1,3] # return 5 
hp6 = [10,7,9,5,4,3,6] 

# print(poscount(hp1,0,1))
# print(poscount(hp3,0,7))
# print(poscount(hp3,2,7))
# print(poscount(hp4,0,3))
# print(poscount(hp4,1,3))
# print(poscount(hp5,0,6))
# print(kposcount(hp5,0,6,5))
# print(poscount(hp5,1,6))
# print(poscount(hp5,2,6))
print(poscount(hp6,0,7))
print(kposcount(hp6,0,7,8))