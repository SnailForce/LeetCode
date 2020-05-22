class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1 = len(haystack)
        l2 = len(needle)
        if l2 == 0:
            return 0
        if l1 < l2:
            return -1
        for i in range(l1 - l2 + 1):
            if haystack[i] == needle[0]:
                if haystack[i:i + l2] == needle:
                    return i
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
