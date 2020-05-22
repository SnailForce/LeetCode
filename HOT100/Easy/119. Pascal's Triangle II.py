from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        d = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        if 0 <= rowIndex <= 3:
            return d[rowIndex]

        pre = d[-1]
        print(pre)
        for i in range(4, rowIndex + 1):
            cur = [1]
            for j in range(1, i):
                cur.append(pre[j - 1] + pre[j])
            cur.append(1)
            pre = cur[:]
        return pre


if __name__ == "__main__":
    s = Solution()
    print(s.getRow(3))
