from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        if len(nums) <= 1:
            return TreeNode(nums[0])

        mid = nums[len(nums) // 2]
        root = TreeNode(mid)
        root.left = self.sortedArrayToBST(nums[:len(nums) // 2])
        root.right = self.sortedArrayToBST(nums[len(nums) // 2 + 1:])
        return root

    def printTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            cur = stack.pop(0)
            if cur:
                res.append(cur.val)
                stack.append(cur.left)
                stack.append(cur.right)
            else:
                res.append(None)
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [-10, -3, 0, 5, 9]
    root = s.sortedArrayToBST(nums)
    res = s.printTree(root)
    print(res)
