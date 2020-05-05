class Solution:
    def convertToTitle(self, n: int) -> str:
        if n <= 0:
            return ""
        res = []
        d = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        while n:
            res.append(n % 26)
            minus = 26 if n % 26 == 0 else n % 26
            n = (n - minus) / 26
        res = [int(i) for i in res]
        for i in range(len(res)):
            res[i] = d[res[i]]
        return ''.join(res[::-1])

    def convertToTitle2(self, n: int) -> str:
        if n <= 0:
            return ""
        res = []
        while n:
            n -= 1
            cur = n % 26
            res.append(chr(ord('A') + cur))
            n //= 26
        return ''.join(res[::-1])


if __name__ == "__main__":
    s = Solution()
    print(s.convertToTitle(701))
    print(s.convertToTitle(28))
    print(s.convertToTitle(1))
    print(s.convertToTitle(26))
    print(s.convertToTitle(26 * 24))
