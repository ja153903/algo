"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

=== Solution ===

Given that we're looking for the largest profit with one trade, we want to keep track of the min and max prices such that
the index of the min price is less than the index of the max price
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_buy = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            min_buy = min(min_buy, prices[i])
            max_profit = max(max_profit, prices[i] - min_buy)

        return max_profit
