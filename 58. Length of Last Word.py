class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(' ')[-1])

    def lengthOfLastWord2(self, s: str) -> int:
        r = s[::-1]
        index1, index2 = 0, 0
        t = 0
        for i in r:
            if i != ' ':
                index1 = t
                break
            t += 1
        # print(index1)
        t = index1
        # print(r[index1:])
        for i in r[index1:]:
            if i == ' ':
                index2 = t
                return index2 - index1
            t += 1

        return len(s) - index1


if __name__ == '__main__':
    s = Solution()
    # print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("abc  "))  # " a"
    print(s.lengthOfLastWord("a "))  # " a"
    print(s.lengthOfLastWord(" a "))
    print(s.lengthOfLastWord("  "))
    print(s.lengthOfLastWord(""))
