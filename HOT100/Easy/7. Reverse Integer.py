class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            y = int(str(x)[::-1])
        else:
            y = -int(str(-x)[::-1])
        if y > 0x7fffffff or y < -0x80000000:
            return 0
        else:
            return y

    def reverse2(self, x: int) -> int:
        if x > 0:
            flag = 1
        else:
            flag = -1
        x = abs(x)
        y = 0
        while x:
            t = x % 10
            x = x // 10
            y = y * 10 + t
        y *= flag
        if (y > 0x7fffffff) or (y < -0x80000000):
            return 0
        return y


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(1534236469))
