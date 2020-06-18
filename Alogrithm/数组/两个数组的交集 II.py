from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = []
        for c in c1:
            if c in c2:
                num = min(c1[c], c2[c])
                if num > 0:
                    res += [c] * num
        return res

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return None
        m = {}
        for num in nums1:
            if num not in m.keys():
                m[num] = 1
            else:
                m[num] += 1
        res = []
        for num in nums2:
            if num in m.keys() and m[num] > 0:
                res.append(num)
                m[num] -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
    print([2] * 3)
