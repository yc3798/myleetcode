# TODO: Best time to buy and sell I review
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        changes = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        
        maxprofit = 0
        for k in changes:
            if k > 0:
                maxprofit += k
        return maxprofit
