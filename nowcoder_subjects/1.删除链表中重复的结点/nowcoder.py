# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        p = pHead.next
        if p.val != pHead.val:
            pHead.next = self.deleteDuplication(pHead.next)
        else:
            while pHead.val == p.val and p.next is not None:
                p = p.next
            if p.val != pHead.val:
                pHead = self.deleteDuplication(p)
            else:
                return None
        return pHead
