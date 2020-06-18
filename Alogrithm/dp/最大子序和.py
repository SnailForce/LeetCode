from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


    def maxSubArray2(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for num in nums:
            curSum += num
            maxSum = max(curSum, maxSum)
            if curSum < 0:
                curSum = 0           
        return maxSum


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray2([-1]))
    print(s.maxSubArray2([-2, 1]))
    print(s.maxSubArray2([-1, -2]))
