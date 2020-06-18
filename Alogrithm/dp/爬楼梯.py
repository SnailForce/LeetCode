class Solution:
    diu = [0, 1, 2]

    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        i = 2
        dp = {0: 1, 1: 1}
        while i < n + 1:
            dp[i] = dp[i - 1] + dp[i - 2]
            i += 1
        return dp[n]

    def climbStairs2(self, n: int) -> int:
        if n >= len(self.diu):
            self.diu.append(self.climbStairs(n - 1) + self.climbStairs(n - 2))
        return self.diu[n]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))
