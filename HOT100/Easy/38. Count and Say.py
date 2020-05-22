class Solution:
    def countAndSay(self, n: int) -> str:
        s = ['', '1', '11', '21', '1211']
        if n < 4:
            return s[n]
        for _ in range(5, n + 1):
            t = s[-1]
            r = ""
            num = 1
            for i in range(len(t) - 1):
                if t[i] == t[i + 1]:
                    num += 1
                    if i == len(t) - 2:
                        r += str(num) + t[i]
                else:
                    r += str(num) + t[i]
                    num = 1
                    if i == len(t) - 2:
                        r += '1' + t[i + 1]
            s.append(r)
        return s[n]


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(4))
    print(s.countAndSay(10))
