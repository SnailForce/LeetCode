class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]

    def isPalindrome3(self, s: str) -> bool:
        if not s:
            return True
        import re
        s = "".join(re.findall("[A-Za-z0-9]", s)).lower()
        return s == s[::-1]

    def isPalindrome2(self, s: str) -> bool:
        if not s or s.isspace():
            return True
        cur = ""
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRDSTUVWXYZ1234567890":
                cur += i.lower()
        return cur == cur[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("  "))
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
    print(s.isPalindrome(""))
    print(123)
    # t == "" or t == None -> if not t: print('yes')
