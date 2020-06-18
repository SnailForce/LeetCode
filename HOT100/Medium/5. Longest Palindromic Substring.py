class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isH(cur: str) -> bool:
            return cur == cur[::-1]
        if not s:
            return ""
        curS = s[0]
        curLen = 1
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                u = s[i:j]
                if isH(u) and curLen < len(u):
                    curS = u
                    curLen = len(u)
        return curS

                                


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
