from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        cur1, cur2 = 0, 0
        res = 0
        for i in range(len(prices) - 1):
            cur1, cur2 = prices[i], prices[i + 1]
            if cur1 < cur2:
                res += cur2 - cur1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([1, 2, 3, 4, 5]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
