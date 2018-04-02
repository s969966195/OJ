# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        last = pRoot
        res = []
        everyres = []
        tmp = deque([pRoot])
        while tmp:
            t = tmp.pop()
            everyres.append(t.val)
            if t.left:
                tmp.appendleft(t.left)
            if t.right:
                tmp.appendleft(t.right)
            if t == last:
                res.append(everyres)
                everyres = []
                if tmp:
                    last = tmp[0]
        return res
