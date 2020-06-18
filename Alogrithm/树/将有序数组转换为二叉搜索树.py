from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.test(nums, 0, len(nums) - 1)

    def test(self, nums: List[int], u1: int, u2: int) -> TreeNode:
        if u1 > u2:
            return None
        mid = (u1 + u2) // 2
        r = TreeNode(nums[mid])
        r.left = self.test(nums, u1, mid - 1)
        r.right = self.test(nums, mid + 1, u2)
        return r