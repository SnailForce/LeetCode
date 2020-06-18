from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
    def containsDuplicate2(self, nums: List[int]) -> bool:
        if not nums:
            return False
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
        for s in m.keys():
            if m[s] > 1:
                return True
        return False