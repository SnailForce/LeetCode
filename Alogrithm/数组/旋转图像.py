from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import copy
        cur = copy.deepcopy(matrix)
        d = len(matrix) - 1
        for i in cur:
            print(i)
            k = 0
            for j in range(len(matrix)):
                matrix[j][d] = i[k]
                k += 1
            d -= 1


if __name__ == "__main__":
    s = Solution()
    t = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s.rotate(t)
    print(t)

        
