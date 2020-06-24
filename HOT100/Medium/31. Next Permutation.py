from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if not nums:
            return None
        u = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                u = False
        if u:
            nums[:] = nums[::-1]
            return None
        cur1 = len(nums) - 1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                cur1 = i - 1
                break
        cur2 = len(nums) - 1
        for j in range(len(nums) - 1, cur1, -1):
            if nums[j] > nums[cur1]:
                cur2 = j
                break
        nums[cur1], nums[cur2] = nums[cur2], nums[cur1]
        nums[cur1 + 1 :] = nums[-1:cur1:-1]
        return None
        


if __name__ == "__main__":
    s = Solution()
    cur = [5, 4, 6, 1, 2]
    s.nextPermutation(cur)
    print(cur)
    cur = [1, 2, 3]
    s.nextPermutation(cur)
    print(cur)
    cur = [1, 3, 2]
    s.nextPermutation(cur)
    print(cur)
