from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = int(1e9)
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(price - min_price, max_profit)
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0
        if sorted(prices, reverse=True) == prices:
            return 0
        res = 0
        for i in range(len(prices) - 1):
            cur = max(prices[i + 1:]) - prices[i]
            res = cur if cur > res else res
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
