from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        single_board = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = board[i][j]
                if num not in rows[i]:
                    rows[i].append(num)
                else:
                    return False
                if num not in cols[j]:
                    cols[j].append(num)
                else:
                    return False
                single_index = i // 3 * 3 + j // 3
                if num not in single_board[single_index]:
                    single_board[single_index].append(num)
                else:
                    return False
        return True

    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        def func(cur: List[str]) -> bool:
            res = [int(i) for i in cur if i != '.']
            return len(res) == len(set(res))
        for cur in board:
            if not func(cur):
                return False
        for i in range(9):
            cur = [j[i] for j in board]
            if not func(cur):
                return False
        for i in range(9):
            cur = []
            s1, s2 = i//3*3, i % 3*3
            cur.append(board[s1][s2])
            cur.append(board[s1][s2 + 1])
            cur.append(board[s1][s2 + 2])
            cur.append(board[s1 + 1][s2])
            cur.append(board[s1 + 1][s2 + 1])
            cur.append(board[s1 + 1][s2 + 2])
            cur.append(board[s1 + 2][s2])
            cur.append(board[s1 + 2][s2 + 1])
            cur.append(board[s1 + 2][s2 + 2])
            if not func(cur):
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku([[".", ".", "4", ".", ".", ".", "6", "3", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], ["5", ".", ".", ".", ".", ".", ".", "9", "."], [".", ".", ".", "5", "6", ".", ".", ".", "."], [
          "4", ".", "3", ".", ".", ".", ".", ".", "1"], [".", ".", ".", "7", ".", ".", ".", ".", "."], [".", ".", ".", "5", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."]]))
    n = [[".", ".", "4", ".", ".", ".", "6", "3", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], ["5", ".", ".", ".", ".", ".", ".", "9", "."], [".", ".", ".", "5", "6", ".", ".", ".", "."], ["4", ".", "3", ".",
                                                                                                                                                                                                      ".", ".", ".", ".", "1"], [".", ".", ".", "7", ".", ".", ".", ".", "."], [".", ".", ".", "5", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    for i in n:
        print(i)
