# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res, tmp = [], []
        last = pRoot
        q = deque([pRoot])
        left_to_right = True
        while q:
            t = q.popleft()
            tmp.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
            if t == last:
                res.append(tmp if left_to_right else tmp[::-1])
                left_to_right = not left_to_right
                tmp = []
                if q:
                    last = q[-1]
        return res
