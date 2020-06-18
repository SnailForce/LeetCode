# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        if not head.next.next:
            cur = head.next
            head.next.next = head
            head.next = None
            return cur
        c = self.reverseList(head.next)
        cu = c
        while cu.next:
            cu = cu.next
        cu.next = head
        head.next = None
        return c
