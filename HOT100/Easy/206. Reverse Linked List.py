# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = None
        while head:
            n = head.next
            head.next = pre
            pre, head = head, n
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return res
