from typing import List


class Solution:
    def test(self, s1: str, s2: str) -> str:
        res = ""
        for i, j in zip(s1, s2):
            if i == j:
                res += i
            else:
                return res
        return res

    @staticmethod
    def test2(s1: str, s2: str) -> str:
        res = ""
        for i, j in zip(s1, s2):
            if i == j:
                res += i
            else:
                return res
        return res

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        r = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(r) != 0:
                r = r[:-1]
        return r

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        r = strs[0]
        for i in strs:
            if len(i) < len(r):
                r = i
        for i in strs:
            # r = self.test(r, i)
            r = Solution.test2(r, i)
            if r is None:
                return ""
        return r

    def t(self, strs: List[str]) -> str:
        print(*strs)
        p1 = zip(*strs)
        for i in p1:
            print(i)
        p = list(zip(*strs))
        print(p)


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix2(["flower", "flow", "flight"]))
    print(s.t(["flower", "flow", "flight"]))
