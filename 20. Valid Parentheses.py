class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        return len(s) == 0

    def isValid3(self, s: str) -> bool:
        m = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for i in s:
            if i in m:
                stack.append(i)
            elif m[stack.pop()] != i:
                return False
        return len(stack) == 1

    def isValid2(self, s: str) -> bool:
        l = len(s)
        if l & 1 == 1:
            return False
        ss = s
        for _ in range(l // 2):
            r = ""
            flag = False
            flag2 = False
            for i in range(len(ss) - 1):
                if (ss[i] == "(" and ss[i + 1] == ")") or (ss[i] == "[" and ss[i + 1] == "]") or (
                        ss[i] == "{" and ss[i + 1] == "}"):
                    flag = True
                    if i == len(ss) - 3:
                        flag2 = True
                    continue
                else:
                    if flag2:
                        r += ss[i + 1]
                        break
                    if flag:
                        flag = False
                        continue
                    else:
                        r += ss[i]
            # print(r)
            ss = r
        if ss == "":
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    # print(s.isValid("()"))
    # print(s.isValid("()[]{}"))
    # print(s.isValid("(]"))
    # print(s.isValid("([)]"))
    # print(s.isValid("{[]}"))
    print(s.isValid("(()("))
