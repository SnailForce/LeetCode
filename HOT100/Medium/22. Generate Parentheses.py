from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        


    def generateParenthesis2(self, n: int) -> List[str]:
        if n == 0:
            return []
        dp = [None for _ in range(n + 1)]
        dp[0] = [""]
        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                t1 = dp[j]
                t2 = dp[i - j - 1]
                for s1 in t1:
                    for s2 in t2:
                        cur.append('(' + s1 + ')' + s2)
            dp[i] = cur
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
