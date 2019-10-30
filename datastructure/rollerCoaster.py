# Ch9 Selection 
# find min, max in O(n), linear 
# def findminmax(A):

def rollercoaster(A):
	n = len(A)
	if n == 1:
		return A 
	m = median_of_medians(A, (n-1)//2) # == SELECT 
	B = [None for i in range(n)]
	i = 0
	j = 1
	print(m)
	for x in A: # put smaller at even index, larger at odd index 
		print(B)
		if x <= m:
			B[i] = x
			i += 2
		elif x>m:
			B[j] = x
			j+= 2
	print(B)



def median_of_medians(A, i):

    #divide A into sublists of len 5
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)//2]
    else:
        #the pivot is the median of the medians
        pivot = median_of_medians(medians, len(medians)//2)

    #partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low,i)
    elif i > k:
        return median_of_medians(high,i-k-1)
    else: #pivot = k
        return pivot


def buildRollerCoaster(A):
	n = len(A)
	if n == 1:
		return A
	if n == 2:
		return [min(A),max(A)]
	for i in range(1,n):
		if i % 2 != 0:
			if A[i] < A[i-1]:
				temp = A[i-1]
				A[i-1] = A[i]
				A[i] = temp 
			if A[i] < A[i+1]:
				temp = A[i+1]
				A[i+1] = A[i]
				A[i] = temp 
	print(A)

A1 = [1,2,3,4,5]
A2 = [5,4,3,2,1]
A3 = [1,2,3,4]
A4 = [2,1]
A5 = [3,2,1]
buildRollerCoaster(A1)
buildRollerCoaster(A2)
print(median_of_medians(A1, 2))
rollercoaster(A1)
rollercoaster(A3)
rollercoaster(A4)
rollercoaster(A5)