from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [nums]
        n = len(nums)
        res = []

        def backtrack(u: int) -> None:
            if u == n:
                res.append(nums[:])
                return None
            for i in range(u, len(nums)):
                nums[u], nums[i] = nums[i], nums[u]
                backtrack(u + 1)
                nums[u], nums[i] = nums[i], nums[u]
        
        backtrack(0)
        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 1:
            return [nums]
        path = []
        res = []
        size = len(nums)
        used = [False for _ in range(len(nums))]

        def dfs(nums: List[int], depth: int, path: List[int]) -> None:
            if depth == size:
                res.append(path[:])
                return None
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, depth + 1, path)
                    used[i] = False
                    path.pop()

        dfs(nums, 0, path)
        return res


if __name__ == "__main__":
    s = Solution()
    print(len(s.permute([1, 2, 3])))
