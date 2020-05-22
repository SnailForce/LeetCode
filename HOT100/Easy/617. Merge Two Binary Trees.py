# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2:
            return t2 if not t1 else t1
        stack = [(t1, t2)]
        while stack:
            cur1, cur2 = stack.pop()
            cur1.val += cur2.val
            if cur1.left is not None and cur2.left is not None:
                stack.append((cur1.left, cur2.left))
            elif cur1.left is None:
                cur1.left = cur2.left
            if cur1.right is not None and cur2.right is not None:
                stack.append((cur1.right, cur2.right))
            elif cur1.right is None:
                cur1.right = cur2.right
        return t1

    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left, t1.right = self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right)
        return t1
