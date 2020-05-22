class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)

    def mySqrt2(self, x: int) -> int:
        left = 0
        right = x >> 1
        while left <= right:
            mid = left + ((right - left) >> 1)  # 向下取整
            square1 = mid ** 2
            square2 = (mid + 1) ** 2
            if square1 <= x < square2:
                return mid
            elif square1 < x:
                left = mid + 1
            else:
                right = mid - 1
        return x


if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(0))
    print(s.mySqrt(4))
    print('--')
    print(s.mySqrt(8))
    # print(s.mySqrt(1383856179))
