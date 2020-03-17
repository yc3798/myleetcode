# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # binary search 
        i = 1
        j = n
        while True:
            if i + 1 == j:
                if isBadVersion(i):
                    return i
                else: # isBadVersion(j):
                    return j
            
            mid = i + (j - i) // 2
            
            if isBadVersion(i):
                return i
            
            elif isBadVersion(mid):
                # search left part 
                i, j = i, mid
            else:
                # serach right part 
                i, j = mid, j