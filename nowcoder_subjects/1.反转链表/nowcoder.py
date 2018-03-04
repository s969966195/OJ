# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        newHead = None
        while pHead is not None:
            temp = pHead.next
            pHead.next = newHead
            newHead = pHead
            pHead = temp
        return newHead
