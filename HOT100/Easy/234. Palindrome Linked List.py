# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        stack = []
        while fast.next and fast.next.next:
            stack.append(slow.val)
            slow, fast = slow.next, fast.next.next
        if not stack:
            return head.val == head.next.val
        cur = slow.next
        while cur:
            if cur.val == stack.pop():
                cur = cur.next
            else:
                return False
        return True

    def isPalindrome3(self, head: ListNode) -> bool:
        if not head:
            return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        pre, cur = None, slow.next
        slow.next = None
        while cur:
            n = cur.next
            cur.next = pre
            pre = cur
            cur = n
        n1, n2 = head, pre
        while n1 and n2:
            if n1.val == n2.val:
                n1, n2 = n1.next, n2.next
            else:
                return False
        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        if not head:
            return True
        cur1 = self.printListNode(head)
        cur2 = self.printListNode(self.test(head))
        return cur1 == cur2

    def test(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = self.test(head.next)
        head.next.next = head
        head.next = None
        return cur

    def printListNode(self, head: ListNode) -> List[int]:
        if not head:
            return
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res


if __name__ == "__main__":
    s = Solution()
    s1 = ListNode(1)
    s2 = ListNode(2)
    s1.next = s2
    print(s.isPalindrome(s1))
