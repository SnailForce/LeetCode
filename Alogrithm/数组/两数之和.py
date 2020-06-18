from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        m = {}
        for i in range(len(nums)):
            cur = target - nums[i]
            if cur in m.keys():
                return [m[cur], i]
            else:
                m[nums[i]] = i
