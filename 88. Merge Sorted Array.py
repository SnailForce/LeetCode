from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:]
        nums1.sort()

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        target_index = m + n - 1
        cur1 = m - 1
        cur2 = n - 1
        while cur1 >= 0 and cur2 >= 0:
            if nums1[cur1] >= nums2[cur2]:
                nums1[target_index] = nums1[cur1]
                cur1 -= 1
            else:
                nums1[target_index] = nums2[cur2]
                cur2 -= 1
            target_index -= 1
        if cur2 >= 0:
            nums1[:cur2 + 1] = nums2[:cur2 + 1]
        print(nums1)


if __name__ == "__main__":
    s = Solution()
    s.merge2([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    s.merge2([0], 0, [1], 1)
    s.merge2([2, 0], 1, [1], 1)
