class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def climbStairs2(self, n: int) -> int:
        s = {'1': 1, '2': 2, '3': 3, '4': 5, '5': 8}
        for i in range(6, n + 1):
            s[str(i)] = s[str(i - 2)] + s[str(i - 1)]
        return s[str(n)]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(10))
