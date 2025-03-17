# problem 122
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, total_profit = prices[0], 0, [0]
        for price in prices[1:]:
            if price < sell:
                total_profit.append(0)
                buy = price
                sell = 0
            if price < buy:
                buy = price
            elif buy < price:
                if total_profit[-1] < price - buy:
                    total_profit[-1] = price - buy
                    sell = price
        return sum(total_profit)
