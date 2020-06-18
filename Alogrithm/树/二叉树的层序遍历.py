from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        stack = [root]
        res = []
        while stack:
            u = []
            tmp = []
            while stack:
                cur = stack.pop(0)
                if cur:
                    u.append(cur.val)
                    if cur.left:
                        tmp.append(cur.left)
                    if cur.right:
                        tmp.append(cur.right)
            stack = tmp
            res.append(u)
        return res

