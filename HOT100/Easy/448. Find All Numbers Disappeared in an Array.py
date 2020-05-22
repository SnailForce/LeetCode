from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= - 1
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        print(res)
        return res

    def findDisappearedNumbers3(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        nums = set(nums)
        res = []
        for num in range(1, n + 1):
            if num not in nums:
                res.append(num)
        return res

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        t = {}
        for num in nums:
            t[num] = 1
        res = []
        for num in range(1, len(nums) + 1):
            if num not in t:
                res.append(num)
        return res


if __name__ == "__main__":
    s = Solution()
    s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
