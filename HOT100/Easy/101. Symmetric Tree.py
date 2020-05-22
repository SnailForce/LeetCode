# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left != None and root.right != None:
            left_res, right_res = [], []
            self.f(root.left, left_res, 0)
            self.f(root.right, right_res, 1)
            print(left_res, right_res)
            return left_res == right_res
        elif root.left == root.right == None:
            return True
        else:
            return False

    def f(self, root: TreeNode, res: [int], flag: bool) -> None:
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                if flag == 0:
                    stack.append(cur.left)
                    stack.append(cur.right)
                else:
                    stack.append(cur.right)
                    stack.append(cur.left)
            else:
                res.append(None)

    def isSymmetric2(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)


if __name__ == "__main__":
    root = TreeNode(1)
    r1 = TreeNode(2)
    r2 = TreeNode(2)
    r3 = TreeNode(3)
    r4 = TreeNode(4)
    r5 = TreeNode(4)
    r6 = TreeNode(3)
    root.left = r1
    root.right = r2
    r1.left = r3
    r1.right = r4
    r2.left = r5
    r2.right = r6

    s = Solution()
    s.isSymmetric(root)
