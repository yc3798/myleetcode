class Solution(object):
    #TODO: USE RECURSION! 
    # Brute force: time limit exceeded 
    # O(n^2): compare every 2 combo 
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # if found global inversion return False 
        i = 0
        j = 1 
        n = len(A)
        if len == 1:
            return True
        while i < n-1:
            if A[i] > A[j]:
                if j - i > 1:
                    return False #found non-local inversions
                # increment or reset j 
            if j == n-1:
                i += 1
                j = i+1
            else:
                j += 1
        return True
                
        
