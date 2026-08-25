class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            profit = max(profit, prices[i]-minval)
            minval = min(minval, prices[i])
        return profit
        