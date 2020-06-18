from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        for i in len(l):
            if digits[l - i - 1] == 9:
                digits[l - i - 1] = 0
                if l - i - 1 == 0:
                    digits.insert(0, 1)
            else:
                digits[l - i - 1] += 1
                break
        return digits

    def plusOne2(self, digits: List[int]) -> List[int]:
        if not digits:
            return None
        cur = 1
        res = []
        for num in digits[::-1]:
            num += cur
            cur = 1 if num > 9 else 0
            res.append(num if num < 10 else num-10)
        if cur == 1:
            res.append(1)
        return res[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1, 2, 3]))
    print(s.plusOne([1, 2, 9]))
    print(s.plusOne([0]))
    print(s.plusOne([9, 9, 9]))
