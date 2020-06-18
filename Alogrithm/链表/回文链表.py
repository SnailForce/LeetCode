# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        cur = slow.next if fast else slow

        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        cur = pre

        while head and cur:
            if head.val != cur.val:
                return False
            head, cur = head.next, cur.next
        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        cur = []
        while head:
            cur.append(head.val)
            head = head.next
        return cur == cur[::-1]
