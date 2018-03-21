# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    __is_balanced = True

    def getDepth(self, pRoot):
        if pRoot is None:
            return 0
        left_depth = self.getDepth(pRoot.left)
        right_depth = self.getDepth(pRoot.right)
        if abs(left_depth-right_depth) > 1:
            self.__is_balanced = False
        return left_depth+1 if left_depth > right_depth else right_depth+1

    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.getDepth(pRoot)
        return self.__is_balanced
