from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while True:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        HashMap = {}
        for i, num in enumerate(numbers):
            if HashMap.get(target - num) is not None:
                return [HashMap.get(target - num) + 1, i + 1]
            else:
                HashMap[num] = i
        return []
