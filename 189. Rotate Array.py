from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        count, start = 0, 0
        while count < len(nums):
            cur = (start + k) % len(nums)
            pre = nums[start]
            while start != cur:
                nums[cur], pre = pre, nums[cur]
                cur = (cur + k) % len(nums)
                count += 1
            nums[start] = pre
            count += 1
            start += 1

    def rotate3(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums.reverse()
        nums[:] = list(reversed(nums[:k])) + list(reversed(nums[k:]))

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= l
        nums[:] = nums[-k:] + nums[: - k]


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums, 3)
    print(nums)
