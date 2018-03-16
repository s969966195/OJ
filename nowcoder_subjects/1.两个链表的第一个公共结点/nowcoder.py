# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here

        #
        # 两个循环
        #
        '''
        list1, list2 = [], []
        node1, node2 = pHead1, pHead2
        while node1:
            list1.append(node1.val)
            node1 = node1.next

        while node2:
            if node2.val in list1:
                return node2
            else:
                node2 = node2.next
        '''
        node1, node2 = pHead1, pHead2
        while node1 != node2:
            node1 = pHead2 if node1 is None else node1.next
            node2 = pHead1 if node2 is None else node2.next
        return node1
