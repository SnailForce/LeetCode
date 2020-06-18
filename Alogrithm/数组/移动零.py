from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        cur = 0
        for num in nums:
            if num != 0:
                nums[cur] = num
                cur += 1
        for i in range(cur, len(nums)):
            nums[i] = 0

if __name__ == "__main__":
    s = Solution()
    n = [0, 1, 0, 3, 12]
    s.moveZeroes(n)
    print(n)