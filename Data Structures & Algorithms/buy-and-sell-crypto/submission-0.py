class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        low = prices[0]
        high = prices[0]
        profit = 0

        for i in range(1, n):
            if prices[i] < low:
                low = prices[i]
                high = prices[i]
            else:
                high = max(high, prices[i])

            profit = max(profit, high-low)

        return profit