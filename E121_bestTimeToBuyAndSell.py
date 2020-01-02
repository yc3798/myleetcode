class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) using dynamic programming 
        n = len(prices)
        if n <= 1:
            return 0
        if n == 2:
            return max(0, prices[1] - prices[0])
        
        # turn into maxsum problem 
        changes = [(prices[i] - prices[i-1]) for i in range(1,n)]
        # print(changes)
        globalmax = max(changes[0],0)
        localmax = changes[0]
        for i in range(1,n-1):
            localmax = max(localmax+changes[i], changes[i])
            globalmax = max(globalmax, localmax)
        return globalmax
            
        
        
