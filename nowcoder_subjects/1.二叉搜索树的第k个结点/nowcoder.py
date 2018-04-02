# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 返回对应节点TreeNode
    '''
    中序遍历
    '''
    index = 0

    def KthNode(self, pRoot, k):
        # write code here
        if pRoot is None:
            return None
        # 左
        node = self.KthNode(pRoot.left, k)
        if node is not None:
            return node
        # 根
        self.index += 1
        if self.index == k:
            return pRoot
        # 右
        node = self.KthNode(pRoot.right, k)
        if node is not None:
            return node
