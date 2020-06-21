from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for f in range(n):
            if f > 0 and nums[f] == nums[f - 1]:
                continue
            t = n - 1
            cur = -nums[f]
            for s in range(f + 1, n):
                if s > f + 1 and nums[s] == nums[s - 1]:
                    continue
                while s < t and nums[s] + nums[t] > cur:
                    t -= 1
                if s == t:
                    break
                if nums[s] + nums[t] == cur:
                    res.append([nums[f], nums[s], nums[t]])
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
