# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        import queue
        q = queue.Queue()
        q.put(root)
        length = 0
        while not q.empty():
            cur = q.get()
            q_cur = []
            if cur.left:
                q.put(cur.left)
                q_cur.append(cur.left.val)
            else:
                q_cur.append(-1)
            if cur.right:
                q.put(cur.right)
                q_cur.append(cur.right.val)
            else:
                q_cur.append(-1)
