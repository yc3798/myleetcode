# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


# Counting Sort

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0, 0, 0]

        for i in nums:
        	count[i] += 1
        # print(count)
        num = 0
        i = 0
        for n in count:
        	nums[i:i+n+1] = [num for k in range(n)]
        	i += n
        	num += 1

        print(nums)
Solution().sortColors([2,0,2,1,1,0])


