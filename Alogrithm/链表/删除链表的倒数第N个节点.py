# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        i, j = dummy, dummy
        count = 0
        while i:
            i = i.next
            count += 1
            if count > n + 1:
                j = j.next
        j.next = j.next.next
        return dummy.next

    def removeNthFromEnd3(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        length -= n
        cur = dummy
        while length > 0:
            length -= 1
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        cur = head
        pre = head
        res = count - n
        if res == 0:
            return head.next
        while cur:
            res -= 1
            if res == -1:
                if cur.next:
                    cur.val = cur.next.val
                    cur.next = cur.next.next
                else:
                    pre.next = None
            pre = cur
            cur = cur.next
        return head
