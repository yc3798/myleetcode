class Solution:
    # contmax, contmin: max/min product ending at current index 
    # maxprod: max subarray product so far 
    # for each num:
    # nextcontmax = max(num, contmin * num, contmax * num)
    # nextcontmin = min(num, contmax * num, contmin * num)
    # maxprod = max(nextcontmax, maxprod)
    def maxProduct(self, nums: List[int]) -> int:
        contmax = maxprod = contmin = None
        
        for num in nums:
            if maxprod is None:
                 contmax = maxprod = contmin = num
            else:
                # coutmax = either include num, or just num, or countmin * num 
                nextcontmax = max(num, contmin * num, contmax * num)
                nextcontmin = min(num, contmax * num, contmin * num)
                maxprod = max(nextcontmax, maxprod)
                
                contmax, contmin = nextcontmax, nextcontmin
        return maxprod