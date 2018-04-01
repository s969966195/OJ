# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot is None:
            return True

    def comRoot(self, left, right):
        if left is None:
            return right is None
        if right is None:  # 左子树不空，右子树空
            return False
        if left.val != right.val:
            return False
        return self.comRoot(left.right, right.left) and self.comRoot(left.left, right.right)
