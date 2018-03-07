# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        head = pHead
        p_head = None
        new_head = None

        random_dic = {}
        old_new_dic = {}

        while head:
            node = RandomListNode(head.label)
            node.random = head.random
            old_new_dic[id(head)] = id(node)
            random_dic[id(node)] = node
            head = head.next

            if new_head:
                new_head.next = node
                new_head = new_head.next
            else:
                new_head = node
                p_head = node

        new_head = p_head
        while new_head:
            if new_head.random != None:
                new_head.random = random_dic[old_new_dic[id(new_head.random)]]
            new_head = new_head.next
        return p_head
