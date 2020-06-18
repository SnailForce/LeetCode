from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        if p2 >= 0:
            nums1[:p2+1] = nums2[:p2+1]

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tmp = nums1[:m]
        nums1[:] = []
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if tmp[p1] < nums2[p2]:
                nums1.append(tmp[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1 + p2:] = tmp[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]


if __name__ == "__main__":
    s = Solution()
    n1 = [1, 2, 3, 0, 0, 0]
    n2 = [2, 5, 6]
    s.merge(n1, 3, n2, 3)
    print(n1)
    n1 = [2, 0]
    n2 = [1]
    s.merge2(n1, 1, n2, 1)
    print(n1)
