from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        tmp = []
        candidates.sort()

        def helper(candidates: List[int], i: int, target: int, tmp: List[int]) -> None:
            if target == 0:
                res.append(tmp[:])
                return None
            if i == len(candidates) or candidates[i] > target:
                return None
            tmp.append(candidates[i])
            helper(candidates, i, target - candidates[i], tmp)
            tmp.pop()
            helper(candidates, i + 1, target, tmp)

        helper(candidates, 0, target, tmp)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        candidates.sort()
        path = []
        res = []
        self.dfs(candidates, 0, len(candidates), target, path, res)
        return res

    def dfs(self, candidates: List[int], u: int, v: int, target: int, path: List[int], res: List[int]) -> None:
        if target == 0:
            res.append(path[:])
            return None
        for index in range(u, v):
            if candidates[index] > target:
                break
            path.append(candidates[index])
            self.dfs(candidates, index, v, target -
                     candidates[index], path, res)
            path.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
    print(s.combinationSum2([2, 3, 6, 7], 7))
