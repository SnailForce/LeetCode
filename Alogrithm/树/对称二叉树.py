# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.test(root.left, root.right)

    def test(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None:
            return right is None
        elif right is None:
            return False
        if left.val == right.val:
            return self.test(left.left, right.right) and self.test(left.right, right.left)
        else:
            return False

    def isSymmetric2(self, root: TreeNode) -> bool:
        if not root or not (root.left or root.right):
            return True
        queue = [root.left, root.right]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            else:
                queue.append(left.left)
                queue.append(right.right)
                queue.append(left.right)
                queue.append(right.left)
        return True
        
