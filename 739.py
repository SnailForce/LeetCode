from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ind = []
        res = [0] * len(T)
        for i, num in enumerate(T):
            if not stack:
                stack.append(num)
                ind.append(i)
            else:
                if stack[-1] < num:
                    while stack and stack[-1] < num:
                        res[ind[-1]] = i - ind[-1]
                        stack.pop()
                        ind.pop()         
                stack.append(num)
                ind.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
