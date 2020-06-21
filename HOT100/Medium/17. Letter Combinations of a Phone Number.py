from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {2: "abc", 3: "def", 4: "ghi", 5: "jkl",
               6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        def backtrack(combination, nextDigit):
            if len(nextDigit) == 0:
                res.append(combination)
            else:
                for s in dic[int(nextDigit[0])]:
                    backtrack(combination + s, nextDigit[1:])
        res = []

        if digits:
            backtrack("", digits)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
