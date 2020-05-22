# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True

        def helper(root: TreeNode) -> int:
            if not root:
                return 0
            left = helper(root.left) + 1
            right = helper(root.right) + 1
            if abs(left - right) > 1:
                self.res = False 
            return max(left, right)
        helper(root)
        return self.res

    def isBalanced2(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [root]
        while stack:
            cur = stack.pop(0)
            stack.append(cur.left)
            stack.append(cur.right)
            if abs(getLength(cur.left) - getLength(cur.right)) <= 1:
                pass
            else:
                return False
        return True

        def getLength(r: TreeNode) -> int:
            if not r:
                return 0
            else:
                return 1 + max(getLength(r.left), getLength(r.right))
