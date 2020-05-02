from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return - 1
        res = 0
        for i in nums:
            res = res ^ i
        return res


if __name__ == "__main__":
    s = Solution()
    s.singleNumber([2, 2, 1])
    s.singleNumber([4, 1, 2, 1, 2])
    s.singleNumber([1])
    s.singleNumber([2])
