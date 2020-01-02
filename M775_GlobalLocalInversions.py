# Medium 775. Global and Local Inversions
# We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
# The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].
# The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].
# Return true if and only if the number of global inversions is equal to the number of local inversions.

# Example 1:

# Input: A = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion, and 1 local inversion.
# Example 2:

# Input: A = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions, and 1 local inversion.
# Note:

# A will be a permutation of [0, 1, ..., A.length - 1].
# A will have length in range [1, 5000].
# The time limit for this problem has been reduced.


# Dynamic Programming 
# From back to beg, track minimum 
# only interate A once -> O(n)
import sys 
def isIdealPermutation-DP(A):
    n = len(A)
    if n <= 2:
        return True
    i = n - 1
    globalmin = sys.maxsize
    while i != 1:
        globalmin = min(globalmin, A[i])
        if A[i-2] > globalmin:
            return False
        i -= 1
    return True


    


class Solution(object):
    # Brute force: time limit exceeded 
    # O(n^2): compare every 2 combo 
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # if found global inversion return False 
        i = 0
        j = 2 
        n = len(A)
        if len <= 2:
            return True
        while i < n-1:
            if A[i] > A[j]:
                return False #found non-local inversions
                # increment or reset j 
            if j == n-1:
                i += 1
                j = i+2
            else:
                j += 1
        return True
                
        
