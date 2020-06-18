from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        res = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
                continue
            res = max(res, p - minPrice)
        return res

    def maxProfit2(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        curSum = 0
        maxSum = -0xffffffff
        for p in range(1, len(prices)):
            curSum += (prices[p] - prices[p - 1])
            if curSum < 0:
                curSum = 0
            maxSum = max(maxSum, curSum)
        return maxSum


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
