# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0

        dq = deque()
        layer = 1
        dq.append((pRoot, 1))
        while dq:
            node, layer = dq.popleft()
            deep = layer
            if node.left:
                dq.append((node.left, layer + 1))
            if node.right:
                dq.append((node.right, layer + 1))

        return deep
