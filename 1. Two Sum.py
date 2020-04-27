from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}
        for i, num in enumerate(nums):
            if HashMap.get(target - num) is not None:
                return [HashMap[target - num], i]
            else:
                HashMap[num] = i
        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            r = target - nums[i]
            for j in range(i + 1, l):
                if nums[j] == r:
                    return [i, j]
                else:
                    continue
        return []


if __name__ == '__main__':
    s = Solution().twoSum([3, 2, 4], 7)
    print(s)
