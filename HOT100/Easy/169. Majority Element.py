from typing import List


class Solution:
    # 出现最多的数字和其它数字 二分类
    def majorityElement(self, nums: List[int]) -> int:
        major, occur = 0, 0
        for i in nums:
            if occur == 0:
                major = i
            occur = occur + 1 if major == i else occur - 1
        return major

    def majorityElement3(self, nums: List[int]) -> int:
        r = sorted(nums)
        return r[len(nums)//2]

    def majorityElement2(self, nums: List[int]) -> int:
        s = len(nums) // 2
        m = {}
        for i in nums:
            m[i] = m[i] + 1 if i in m else 1
        res, cur = -1, - 1
        for i, j in m.items():
            if j > cur:
                res, cur = i, j
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
