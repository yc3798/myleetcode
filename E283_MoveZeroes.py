class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # shift non-zero with the first zero, continue 
        if len(nums) < 2:
            return nums
        index = 0
        zero = False
        for i in range(len(nums)):
            if nums[i] != 0:
                if zero:
                    nums[index] = nums[i]
                    nums[i] = 0
                index += 1
            
            elif nums[i] == 0:
                zero = True
