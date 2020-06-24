from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(s: List[str]) -> None:
            if len(s) == n * 2:
                if valid(s):
                    res.append(''.join(s))
            else:
                s.append('(')
                generate(s)
                s[-1] = ')'
                generate(s)
                s.pop()

        def valid(s: str) -> bool:
            bal = 0
            for i in s:
                if i == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
        
        generate([])
        return res

    def generateParenthesis3(self, n: int) -> List[str]:
        res = []
        cur = ''

        def dfs(cur: str, left: int, right: int) -> None:
            if left == 0 and right == 0:
                res.append(cur)
                return
            if right < left:
                return
            if left > 0:
                dfs(cur + '(', left - 1, right)
            if right > 0:
                dfs(cur + ')', left, right - 1)
        dfs(cur, n, n)
        return res

    def generateParenthesis2(self, n: int) -> List[str]:
        if n == 0:
            return []
        dp = [None for _ in range(n + 1)]
        dp[0] = [""]
        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                t1 = dp[j]
                t2 = dp[i - j - 1]
                for s1 in t1:
                    for s2 in t2:
                        cur.append('(' + s1 + ')' + s2)
            dp[i] = cur
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
