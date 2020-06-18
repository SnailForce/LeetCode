def isBadVersion(n: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        u1, u2 = 1, n
        while u1 < u2:
            u = (u1 + u2) // 2
            if isBadVersion(u):
                u2 = u
            else:
                u1 = u + 1
        return u1

    def firstBadVersion2(self, n: int) -> int:
        return self.test(0, n)

    def test(self, s: int, e: int) -> int:
        mid = (s + e) // 2
        if mid == 0:
            return 0 if isBadVersion(mid) else 1
        if not isBadVersion(mid - 1) and isBadVersion(mid):
            return mid
        if isBadVersion(mid):
            return self.test(s, mid - 1)
        else:
            return self.test(mid + 1, e)
