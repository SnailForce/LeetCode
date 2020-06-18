class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup = set()
        maxLen = 0
        curLen = 0
        for i in range(len(s)):
            curLen += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                curLen -= 1
            maxLen = max(maxLen, curLen)
            lookup.add(s[i])
        return maxLen