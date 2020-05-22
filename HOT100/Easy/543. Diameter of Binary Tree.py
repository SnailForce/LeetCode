# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def getDepth(r: TreeNode) -> int:
            if not hasattr(getDepth, 'm'):
                getDepth.m = 0
            if not r:
                return 0
            left, right = getDepth(r.left), getDepth(r.right)
            getDepth.m = max(left + right, getDepth.m)
            return max(left, right) + 1

        getDepth(root)
        return getDepth.m
