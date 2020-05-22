class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)

    def reverseBits1(self, n: int) -> int:
        print(bin(n))
        print(bin(n)[2:])
        print(len(bin(n)[2:]))
        print(('0' * (32 - len(bin(n)[2:])) + bin(n)[2:])[::-1])
        print(int(('0' * (32 - len(bin(n)[2:])) + bin(n)[2:])[::-1]))
        return int(('0' * (32 - len(bin(n)[2:])) + bin(n)[2:])[::-1], 2)

    def reverseBits2(self, n: int) -> int:
        res, power = 0, 31
        while n:
            res += (n & 1) << power
            power -= 1
            n >>= 1
        return res

    def reverseBits3(self, n: int) -> int:
        res = 0
        for i in range(31, -1, -1):
            res += (n & 1) << i
            n >>= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits1(0b00000010100101000001111010011100))
