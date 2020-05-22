from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        for i in range(2, len(nums)):
            nums[i] = nums[i] + max(nums[:i - 1])
        print(nums)
        return max(nums)

    def rob2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0, nums[0]]
        for i in range(2, len(nums) + 1):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i - 1]))
            print(dp)
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.rob2([1, 2, 3, 1]))
    print(s.rob2([2, 7, 9, 3, 1]))
