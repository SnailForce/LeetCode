from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur = nums[0]
        index = 1
        for num in nums:
            if num != cur:
                nums[index] = num
                cur = nums[index]
                index += 1
        return index


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
