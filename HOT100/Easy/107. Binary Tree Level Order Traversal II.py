from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []

        import collections

        queue = collections.deque([root])

        while queue:
            length = len(queue)
            level = []
            for i in range(length):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        
        return res[::-1]


    def levelOrderBottom2(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        res = []
        stack = [[root, 0]]
        while stack:
            cur = stack[0]
            del stack[0]
            if cur[0]:
                res.append([cur[0].val, cur[1]])
                stack.append([cur[0].left, cur[1] + 1])
                stack.append([cur[0].right, cur[1] + 1])
            else:
                res.append(None)
        res = list(filter(None, res))
        r = []
        i = 0
        while i < len(res):
            cur = [res[i][0]]
            j = i + 1
            if j < len(res) and res[i][1] == res[j][1]:
                while res[i][1] == res[j][1]:
                    cur.append(res[j][0])
                    i += 1
                    j += 1
                    if j == len(res):
                        r.append(cur)
                        r = r[::-1]
                        return r
                r.append(cur)
            else:
                r.append(cur)
            i += 1
        r = r[::-1]
        return r
            



if __name__ == "__main__":
    s = Solution()

    root = TreeNode(3)
    r1 = TreeNode(9)
    r2 = TreeNode(20)
    r5 = TreeNode(15)
    r6 = TreeNode(7)
    r7 = TreeNode(100)
    root.left = r1
    root.right = r2
    r2.left = r5
    r2.right = r6
    r6.right = r7

    print(s.levelOrderBottom(root))
