# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        pre = ListNode(None)
        pre.next = head
        fast, slow = pre, pre
        t = 0
        while fast:
            fast = fast.next
            t += 1
            if t >= n + 1:
                slow = slow.next
        slow.next = slow.next.next
        return pre.next
