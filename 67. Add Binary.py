class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary2(self, a: str, b: str) -> str:
        if a == '0':
            return b
        if b == '0':
            return a

        l1, l2 = len(a), len(b)
        if l1 < l2:
            a = '0' * (len(b) - len(a)) + a
        else:
            b = '0' * (len(a) - len(b)) + b
        a = reversed(a)
        b = reversed(b)
        carry = 0
        ret = [0] * max(l1, l2)
        k = 0
        for i, j in zip(a, b):
            # print(i, j)
            ret[k] = int(i) + int(j) + carry
            if ret[k] > 1:
                carry = 1
                ret[k] %= 2
            else:
                carry = 0
            # print("k=" + str(k) + " " + str(ret[k]))
            k += 1
        # print("ret:" + str(ret))
        if carry == 1:
            ret = ret + [1]
        # print(ret)
        res = ""
        for i in ret:
            res += str(i)
        res = res[::-1]
        # print(res)
        return res


if __name__ == "__main__":
    s = Solution()
    # s.addBinary('11', '1')
    s.addBinary('1010', '1011')
