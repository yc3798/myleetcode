# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution:
    # time: T(n) = T(n-1) + n = O(n^2)
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        def helper(lst, perm):
            if len(perm) == len(nums):
                # current permutation finished 
                ans.append(perm)
                return
            for i in range(len(lst)):
                # for each item in lst
                #     if this is not the last item
                if i + 1 < len(lst):
                    helper(lst[:i]+lst[i+1:], perm + [lst[i]])
                else:
                    # last item
                    helper(lst[:i], perm + [lst[i]])
            return
        helper(nums,[])
        return ans