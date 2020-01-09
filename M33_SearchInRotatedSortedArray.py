class Solution:
    # Binary search
    # note that a rotatedly sortly array must have a half that is increasingly sorted 
    # [1,2,3,4,5] -> [4,5,1,2,3], [5,1,2,3,4], [3,4,5,1,2] [1,2,3,4,5]
    # use this property to decide which part we want to search on
    # Use i to track index in recursion call,
    # for example, m = 2, if we search on right, we feed m + i as new i (m + i = first index of right part)
    def search(self, nums, target: int) -> int: 
        return self.searchHelper(nums, target, 0)

    def searchHelper(self, nums, target: int, i) -> int: # use i to track index
        if nums == []:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return i
            else:
                return -1
        n = len(nums)
        # [...|m...]
        m = n // 2

        left = nums[:m]
        right = nums[m:]
        
        # left part is increasingly sorted
        if nums[0] < nums[m]:
            if target >= left[0] and target <= left[-1]: # serach left part
                return self.searchHelper(nums[:m], target, i)
            else:
                return self.searchHelper(nums[m:], target, i + m) # searchHelper right part
        # right part is increasingly sorted
        else:
            if target >= right[0] and target <= right[-1]: # searchHelper the right part
                return self.searchHelper(nums[m:], target, i + m)
            else:
                return self.searchHelper(nums[:m],target, i)


l = [5,1,2,3,4]
print(Solution().search(l, 5))
print(Solution().search(l, 2))
print(Solution().search(l, 0))

l = [3,5,1]
print(Solution().search(l, 1))