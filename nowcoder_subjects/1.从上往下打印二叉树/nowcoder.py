# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res = []
        q = [root]
        while len(q): # 把各节点按顺序加入列表
            temp = q.pop(0)
            res.append(temp.val)
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return res
