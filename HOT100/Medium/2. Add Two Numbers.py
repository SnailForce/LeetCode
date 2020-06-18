# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        pre = ListNode(None)
        u = pre
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            cur = x + y + carry
            carry = cur // 10
            cur = cur % 10
            u.next = ListNode(cur)
            u = u.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            u.next = ListNode(1)
        return pre.next
