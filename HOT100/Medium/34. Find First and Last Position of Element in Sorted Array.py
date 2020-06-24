from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchL() -> int:
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1 if l > len(nums) - 1 or nums[l] != target else l

        def searchR() -> int:
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return - 1 if r < 0 or nums[r] != target else r
        cur1, cur2 = searchL(), searchR()
        return [cur1, cur2] if cur1 != -1 and cur2 != -1 else [-1, -1]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums:
            return res
        l, r = 0, len(nums) - 1
        cur = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                cur = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if cur == -1:
            return res
        u1, u2 = cur, cur
        for i in range(cur, -1, -1):
            if nums[i] == target:
                u1 = i
            else:
                break
        for i in range(cur + 1, len(nums)):
            if nums[i] == target:
                u2 = i
            else:
                break
        return [u1, u2]


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(s.searchRange([5, 7, 7, 8, 8, 10], 6))
    print(s.searchRange([2, 2], 2))
