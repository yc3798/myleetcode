# Greedy: 
# Always pick min(leftmax * rightmax) to form a subtree 
# use an array nums = [(product, max)]
# iterate every time to find minimum product position pos s.t nums[i] * nums[i+1] is minimal possible
# once found, pop the min product pairs to build new tuple (leftmax * rightmax, max(leftmax, rightmax)) and insert at the position 
# add the product to prodsum
# break the loop once the array nums is empty after popping elements

# O(n) time and space

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        prodsum = 0
        if len(arr) <= 1:
            return 0
        
        nums = [(k, k) for k in arr]
        while True:
            minprod = pos = None
            for i in range(len(nums) - 1):
                if minprod is None or nums[i][1] * nums[i+1][1] < minprod:
                    pos = i
                    minprod = nums[i][1] * nums[i+1][1]

            left, lmax = nums.pop(pos)
            right, rmax = nums.pop(pos)
            prodsum += lmax * rmax
            if nums != []:
                nums.insert(pos, (lmax * rmax, max(lmax, rmax)))
            else:
                break

        return prodsum



# Brute force: try all the combinations 
#  review: how many possible combos?
# T(n) = (n - 1)T(n - 1) + n = n! ??? very bad
class SolutionBF:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        self.res = sys.maxsize
        
        def helper(nums, prodsum):
            for i in range(len(nums) - 1):
                cp = [k for k in nums]
                left, lmax, lleaf = cp.pop(i)
                right, rmax, rleaf = cp.pop(i)
                if cp != []:
                    cp.insert(i, (lmax * rmax, max(lmax, rmax), False))
                    helper(cp, prodsum + lmax * rmax)
                else:
                    self.res = min(self.res, prodsum + lmax * rmax)
            return
                
            
        if len(arr) <= 1:
            return 0

        lst = [(k, k, True) for k in arr]
        helper(lst, 0)
        return self.res
