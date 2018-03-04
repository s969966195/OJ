# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        vals = []
        while head is not None:
            vals.append(head)
            head = head.next
        if k>len(l) or k<1:
            return
        return vals[-k]
