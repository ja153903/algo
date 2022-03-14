from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy, max_profit = prices[0], 0

        for i in range(1, len(prices)):
            min_buy = min(prices[i], min_buy)
            max_profit = max(max_profit, prices[i] - min_buy)

        return max_profit
