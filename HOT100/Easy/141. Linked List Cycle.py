# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        fast = head.next
        slow = head
        while fast and fast.next:
            if fast == slow:
                return True
            fast, slow = fast.next.next, slow.next
        return False


    def hasCycle3(self, head: ListNode) -> bool:
        if not head or head.next == None:
            return False
        fast = head.next
        slow = head
        while fast:
            if fast == slow:
                return True
            else:
                fast = fast.next
                if fast == None:
                    return False
                else:
                    fast = fast.next
                    slow = slow.next
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        if not head or head.next == None:
            return False
        s = []
        while head:
            if head in s:
                return True
            else:
                s.append(head)
            head = head.next
        return False

if __name__ == "__main__":
    s = Solution()

    t1 = ListNode(3)
    t2 = ListNode(2)
    t3 = ListNode(0)
    t4 = ListNode(-4)
    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t2
    
    print(s.hasCycle(t1))

    t5 = ListNode(1)
    t6 = ListNode(2)
    t7 = ListNode(3)
    t5.next = t6
    t6.next = t5

    print(s.hasCycle(t5))
    print(s.hasCycle(t7))
