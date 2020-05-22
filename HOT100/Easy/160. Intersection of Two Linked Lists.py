# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            # 假设把if pa != None 改为 if pa.next != None，则可能会出现死循环
            # 原因在于假设AB不相交，pa != pb 条件永远存在
            pA = pA.next if pA != None else headB
            pB = pB.next if pB != None else headA
        return pA

