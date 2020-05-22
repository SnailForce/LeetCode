from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] is not nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

    def removeDuplicates2(self, nums: List[int]) -> int:
        res = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                res += 1
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
            if index == res:
                break
        # print(res)
        # print(nums)
        return res


if __name__ == '__main__':
    s = Solution()
    s.removeDuplicates([1, 1, 1])
    s.removeDuplicates([1, 1, 2])
    s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    s.removeDuplicates([-1, 0, 1, 1, 1, 2, 2, 3, 3, 4])
