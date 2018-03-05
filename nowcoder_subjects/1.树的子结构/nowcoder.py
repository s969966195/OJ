# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.isSubtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def isSubtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1 or pRoot1.val != pRoot2.val:
            return False
        return self.isSubtree(pRoot1.left, pRoot2.left) and self.isSubtree(pRoot1.right, pRoot2.right)
