from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums:
            return None
        cur = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i > cur:
                    nums[cur], nums[i] = nums[i], 0
                cur = cur + 1
        
    def moveZeroes2(self, nums: List[int]) -> None:
        if not nums:
            return None
        index = 0
        for i in nums:
            if i != 0:
                nums[index] = i
                index = index + 1
        nums[index: ] = [0 for _ in range(index, len(nums))]

