# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        m = {0: 1}

        def helper(root: TreeNode, m: dict, sum: int, pathSum: int) -> int:
            if not root:
                return 0
            count = 0
            pathSum += root.val
            count = count + m.get(pathSum - sum, 0)
            m[pathSum] = m.get(pathSum, 0) + 1
            count = helper(root.left, m, sum, pathSum) + \
                helper(root.right, m, sum, pathSum) + count
            m[pathSum] = m[pathSum] - 1
            return count

        return helper(root, m, sum, 0)

    def pathSum3(self, root: TreeNode, sum: int) -> int:
        # 遍历每个节点。关键点：递归，先序遍历。
        # 计算以当前节点为路径终点的所有路径和。关键点：用一个数组path_array保存从根节点到当前节点路径，并同时用一个指针current_end保存当前路径的终点。
        # 对于每一个节点值，其前往根节点的路径是唯一的。如此一来，path_array中，从current_end一直反向遍历到0，便是从当前节点追溯到根节点的过程，这个过程构成了单向的路径（题目中要求的合法路径）。
        # 实际上，current_end的大小，实际上也是树的当前深度（因为是深度遍历）。对于某个时刻的current_end，path_array[current_end:]实际上是无效的。
        # 从当前节点回溯根节点路径唯一
        def path_sum(root, sum_target, path_array, current_end):
            if not root:
                return 0

            current_sum = 0
            count = 0
            path_array[current_end] = root.val    # 当前路径终点的值实际上就是root.val
            for i in range(current_end, -1, -1):
                current_sum += path_array[i]
                if current_sum == sum_target:
                    count += 1

            count_left = path_sum(root.left, sum_target,
                                  path_array, current_end+1)
            count_right = path_sum(root.right, sum_target,
                                   path_array, current_end+1)
            return count + count_left + count_right

        path_array = [0] * 1000
        return path_sum(root, sum, path_array, 0)

    def pathSum2(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        def helper(self, root: TreeNode, sum: int) -> int:
            if not root:
                return 0
            sum = sum - root.val
            return (1 if sum == 0 else 0) + helper(root.left, sum) + helper(root.right, sum)
        return helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
