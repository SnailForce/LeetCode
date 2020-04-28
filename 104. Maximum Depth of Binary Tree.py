# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    s = Solution()

    root = TreeNode(1)
    r1 = TreeNode(2)
    r2 = TreeNode(2)
    r3 = TreeNode(3)
    r4 = TreeNode(4)
    r5 = TreeNode(4)
    # r6 = TreeNode(3)
    root.left = r1
    root.right = r2
    r1.left = r3
    r1.right = r4
    r2.left = r5
    # r2.right = r6

    print(s.maxDepth(root))