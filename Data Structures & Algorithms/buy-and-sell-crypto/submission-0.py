class Solution:
    def maxProfit (self, prices):
        L = 0
        max_profits = 0

        for R in range(len(prices)):

            if prices[R] < prices[L]:
                L = R
            else:
                current_profits = prices[R] - prices[L]
                max_profits = max(current_profits, max_profits)
        return max_profits

            