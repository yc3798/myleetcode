# 53. Maximum Subarray
# Easy
#
# 4845
#
# 180
#
# Favorite
#
# Share
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#
class Solution:
	# O(n)
    def maxSubArray(self, nums):
        n = len(nums)
    	globalmax = nums[0]
    	curr = nums[0]
    	for i in range(1,n):
    		# idea: if sum [... , i] < i, restart curr from i 
    		curr = max(nums[i], curr + nums[i])
    		globalmax = max(globalmax, curr)
    	return globalmax





    # Brute force
    # T(n) = n + (n-1) + (n-2) + ... + 1 = O(n^2)
    #Time limit exceeded 
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        maxsize = max(nums)
        i = 0
        while i < n-1:
            if nums[i] < 0: #we dont want neg 
                i = i + 1 
            s = nums[i]
            for j in range(i+1,n):
                s += nums[j]
                maxsize = max(maxsize,s)
            i += 1
        return maxsize