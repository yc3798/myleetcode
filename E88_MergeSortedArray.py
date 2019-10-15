class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # if m or n is 0 
        if m == 0:
            nums1[:n] = nums2 
        elif n == 0:
            pass 
        else:
            i = m
            for j in range(0,n):
                while i-1 >= 0 and nums2[j] < nums1[i-1]:
                    # shift 
                    nums1[i] = nums1[i-1]
                    i -= 1
                # pos found 
                nums1[i] = nums2[j]
                i = m + j + 1
        