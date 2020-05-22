class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for t in s:
            res = res * 26 + ord(t) - ord('A') + 1
        return res
           

if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("AB"))
    print(s.titleToNumber("ZY"))
