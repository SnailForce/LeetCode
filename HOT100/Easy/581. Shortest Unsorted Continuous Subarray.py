from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        t1, t2 = 0, -1
        s1, s2 = nums[0], nums[-1]
        for i in range(len(nums)):
            if nums[i] < s1:
                t2 = i
            else:
                s1 = nums[i]
            if nums[len(nums) - i - 1] > s2:
                t1 = len(nums) - i - 1
            else:
                s2 = nums[len(nums) - i - 1]
        return t2 - t1 + 1

    def findUnsortedSubarray3(self, nums: List[int]) -> int:
        diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) for a != b]
        return len(diff) and max(diff) - min(diff) + 1

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur = list(sorted(nums))
        count = len(nums)
        for i in range(len(nums)):
            if nums[i] == cur[i]:
                count -= 1
            else:
                break
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == cur[i]:
                count -= 1
            else:
                break
        return count
