from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        flag = False
        index = -1
        j = 0
        if nums[-1] < target:
            nums.append(target)
            return len(nums) - 1
        for i in nums:
            if i == target:
                flag = True
                index = j
                break
            elif i > target:
                index = j
                break
            j += 1
        if flag:
            return index
        else:
            nums.insert(index, target)
            return index


if __name__ == '__main__':
    s = Solution()
    n = [1, 2, 3, 5]
    print(s.searchInsert(n, 3))
    print(n)
    print(s.searchInsert(n, 4))
    print(n)
    print(s.searchInsert(n, 7))
    print(n)