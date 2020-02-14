class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Brute force: sort -> check digit by digit: O(nlogn + n)
        
        # 1. One pass linear sol using hashset to record occurance 
        # d = set(nums)
        # for i in range(len(nums) + 1):
        #     if i not in d:
        #         return i
        # return None

        # 2. calculate sum and return target sum - sum, O(n)
        # target sum = 
        # 0 1 2 3  - 0 2 3 
        target = (len(nums) + 1) * len(nums) / 2 
        return int(target - sum(nums))