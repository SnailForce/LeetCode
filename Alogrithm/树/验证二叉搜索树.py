# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def test(self, root: TreeNode, s: int, e: int) -> bool:
        if not root:
            return True
        if (e is not None and root.val > e) or (s is not None and root.val < s):
            return False
        return self.test(root.left, s, root.val - 1) and self.test(root.right, root.val + 1, e)

        def isValidBST(self, root: TreeNode) -> bool:
            if not root:
                return True
            stack = []
            res = []
            cur = root
            while stack or cur:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
            return res == sorted(res) and len(res) == len(set(res))  # 保证没有相同元素

    def isValidBST2(self, root: TreeNode) -> bool:
        return self.test(root, None, None)
