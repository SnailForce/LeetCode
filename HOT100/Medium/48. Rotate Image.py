from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return None
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) // 2):
                matrix[i][j], matrix[i][len(
                    matrix[i]) - j - 1] = matrix[i][len(matrix[i]) - j - 1], matrix[i][j]

    def rotate2(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return None
        res = [[] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            res[i] = [cur[i] for cur in matrix][::-1]
        matrix[:] = res


if __name__ == "__main__":
    s = Solution()
    cur = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s.rotate(cur)
    print(cur)
