# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List


# 예외 케이스 발생
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        size = len(prices)
        if size == 1:
            return 0

        left, right = size - 2, size - 1

        while left >= 0 and right > 0:
            print(f"start left : {left}, right : {right}")
            profit = prices[right] - prices[left]
            print(f"profit : {profit}")
            if profit > 0:
                if left > 0:
                    left -= 1
                else:
                    right -= 1
                if max_profit < profit:
                    max_profit = profit
            elif profit == 0:
                left -= 1
                right -= 1
            else:
                right -= 1

                if left == right:
                    left -= 1
            print(f"end left : {left}, right : {right}")
            print(f"profit : {profit}")

        return max_profit
