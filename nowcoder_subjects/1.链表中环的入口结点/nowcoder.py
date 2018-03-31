# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        '''
        tempList = []
        p = pHead
        while p:
            if p in tempList:
                return p
            else:
                tempList.append(p)
            p = p.next
        '''
        if pHead is None or pHead.next is None:
            return None
        p1 = pHead
        p2 = pHead
        # x为P1走的路程 n为环内走的路程
        # p2 2x = n+x
        # p1 x
        while p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                p2 = pHead
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                if p1 == p2:
                    return p1
        return None
