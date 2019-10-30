# count inversions with modified Merge Sort: O(nlogn)
# naive approach will take O(n^2)

#[3,5,1,6,2,7] -> (3,1) (3,2) (5,1) (5,2) (6,2) = 5 
#[1,2,3] -> 0
#[1] -> 0
#[2,1] -> 1
import math
def countInversions(arr, p, r): 
	if p<r:
		mid = math.floor((r+p)/2)+1
		print("p, mid, r = ", p, mid, r)
		# print("countleft in ", arr[p:mid+1])
		# print("countleft in ", arr[mid+1:r])
		countleft = countInversions(arr, p, mid+1)
		countright = countInversions(arr, mid, r)
		return countleft+countright+combine(arr,p,mid,r)
	return 0

def combine(arr,p,m,r):
	n1 = mid - p + 1
	n2 = r - mid 
	leftarr = arr[p, mid+1]
	rightarr = arr[mid+1, r]
	combined = []
	i = 0
	j = 0
	count = 0
	for k in range(p, r+1):
		if leftarr[i] > rightarr[j]: #inversion found 
			count += 1
			combined[k] = rightarr[j]
			j += 1
		else:
			combined[k] = leftarr[i]
			i += 1
	return count 

a1 = [2,3,1,4]
test = [a1]
for t in test:
	print(countInversions(a1, 0,3))


