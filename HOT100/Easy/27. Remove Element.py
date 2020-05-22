from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == val:
                res += 1
            else:
                nums[j] = nums[i]
                j += 1
                # nums[:len(nums) - 1] = nums[:i] + nums[i + 1:len(nums)]
        return len(nums) - res


if __name__ == '__main__':
    s = Solution()
    n = [3, 2, 2, 3]
    print(s.removeElement(n, 3))
    print(n)
