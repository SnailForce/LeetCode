class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n:
            count += n // 5
            n //= 5
        return count

    def trailingZeroes2(self, n: int) -> int:
        if n < 5:
            return 0
        count = 0
        for i in range(5, n + 1, 5):
            t = i
            while t:
                if t % 5 == 0:
                    count += 1
                    t //= 5
                else:
                    break
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.trailingZeroes(3))
    print(s.trailingZeroes(5))
    print(s.trailingZeroes(6))
