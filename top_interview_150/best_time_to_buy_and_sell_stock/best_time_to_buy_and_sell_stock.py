# problem 121
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0
        for price in prices[1:]:
            if price < buy:
                buy = price
                profit = 0
            elif buy < price:
                if profit < price - buy:
                    profit = price - buy
        return profit