# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        import queue
        if p == q == None:
            return True
        if p != None and q != None:
            r1, r2 = [p.val], [q.val]
            q1, q2 = queue.Queue(), queue.Queue()
            q1.put(p)
            q2.put(q)
            while q1.empty() == False:
                m = q1.get()
                if m.left:
                    q1.put(m.left)
                    r1.append(m.left.val)
                else:
                    r1.append(-1)
                if m.right:
                    q1.put(m.right)
                    r1.append(m.right.val)
                else:
                    r1.append(-1)
            while q2.empty() == False:
                m = q2.get()
                if m.left:
                    q2.put(m.left)
                    r2.append(m.left.val)
                else:
                    r2.append(-1)
                if m.right:
                    q2.put(m.right)
                    r2.append(m.right.val)
                else:
                    r2.append(-1)
            return r1 == r2
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    n21 = TreeNode(1)
    n22 = TreeNode(2)
    n23 = TreeNode(3)
    n21.left = n22
    n21.right = n23
    s.isSameTree(n1, n21)

    print(p == None)
