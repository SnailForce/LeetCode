# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = [root]
        while stack:
            cur = stack.pop(0)
            if cur.left != None:
                stack.append(cur.left)
            if cur.right != None:
                stack.append(cur.right)
            cur.left, cur.right = cur.right, cur.left
        return root

    def invertTree2(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root