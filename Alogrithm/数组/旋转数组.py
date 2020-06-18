from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        k %= len(nums)

        def fc(n: List[int]) -> None:
            cur = n[-1]
            for i in range(len(n)-1, -1, -1):
                n[i] = n[i - 1]
            n[0] = cur
        for _ in range(k):
            fc(nums)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums, 3)
    print(nums)
