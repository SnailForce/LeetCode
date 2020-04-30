from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        d = [[0], [1], [1, 1], [1, 2, 1]]
        if 0 < numRows <= 3:
            return d[1:numRows + 1]
        for i in range(4, numRows + 1):
            cur = [1]
            for j in range(1, i - 1):
                cur.append(d[i - 1][j - 1] + d[i - 1][j])
            cur.append(1)
            d.append(cur)
        return d[1:]


if __name__ == "__main__":
    s = Solution()
    print(s.generate(4))
    print(s.generate(5))
