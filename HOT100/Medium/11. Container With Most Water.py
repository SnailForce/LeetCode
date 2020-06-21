from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            cur = (r - l) * min(height[r], height[l])
            res = max(cur, res)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
        
