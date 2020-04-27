from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        n = len(digits)
        ret = [0] * n
        carry = 1
        for i in reversed(range(n)):
            s = digits[i] + carry
            ret[i] = s % 10
            carry = s // 10
        if carry:
            ret = [1] + ret
        # print(ret)
        return ret

    def plusOne2(self, digits: List[int]) -> List[int]:
        num = 0
        for i in digits:
            num *= 10
            num += i
        num += 1
        res = []
        while num:
            res.insert(0, num % 10)
            num //= 10
        return res


if __name__ == '__main__':
    s = Solution()
    s.plusOne([1, 2, 3])
    s.plusOne([0])
    s.plusOne([9, 9, 9, 9])
