class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create two arrays of len(nums) + 1
        n = len(nums)
        
        lprod = [1 for i in range(n)]
        rprod = [1 for i in range(n)]

        # compute left product and right product
        # [1,2,3,4,5]
        # left = [1, prev * num[0], prev * num[1]...]
        for i in range(1,n):
            lprod[i] = lprod[i-1] * nums[i-1]
            
        for j in range(n-2, -1, -1):
            rprod[j] = rprod[j+1] * nums[j+1]
            
        ans = [lprod[i] * rprod[i] for i in range(n)]
        return ans