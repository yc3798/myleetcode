class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = i = 0
        temp = 0
        while i < len(nums):
            if i == 0 or nums[i] > nums[i-1]:
                temp += 1
                res = max(res,temp)
            else:
                res = max(res,temp)
                temp = 1
            i += 1
        return res
