class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x ^ y
        count = 0
        while temp:
            if temp & 1:
                count += 1
            temp >>= 1
        return count

    def hammingDistance3(self, x: int, y: int) -> int:
        return str(bin(x ^ y)).count('1')

    def hammingDistance2(self, x: int, y: int) -> int:
        if x == y:
            return 0
        count = 0
        for i in str(bin(x ^ y)[2:]):
            if int(i) == 1:
                count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.hammingDistance(1, 4))
