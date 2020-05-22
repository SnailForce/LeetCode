# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        depth = 0xffffffff
        if not root:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left:
            depth = min(self.minDepth(root.left), depth)
        if root.right:
            depth = min(self.minDepth(root.right), depth)
        return depth + 1

    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        level = 1
        while stack:
            length = len(stack)
            for _ in range(length):
                cur = stack.pop(0)
                if cur:
                    if cur.left == None and cur.right == None:
                        return level
                    stack.append(cur.left)
                    stack.append(cur.right)
            level += 1
