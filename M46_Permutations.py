class Solution:
    # TODO:backtracking technique 
    # time: T(n) = T(n-1) + n = O(n^2)
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        def helper(lst, perm):
            if len(perm) == len(nums):
                ans.append(perm)
                return
            for i in range(len(lst)):
                if i + 1 < len(lst):
                    helper(lst[:i]+lst[i+1:], perm + [lst[i]])
                else:
                    helper(lst[:i], perm + [lst[i]])
            return
        helper(nums,[])
        return ans