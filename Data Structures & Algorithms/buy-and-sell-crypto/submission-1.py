class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        low = prices[0]
        profit = 0

        for i in range(1, n):
            low = min(low, prices[i])
            profit = max(profit, prices[i]-low)

        return profit