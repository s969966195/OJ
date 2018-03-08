# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 处理左子树
        self.Convert(pRootOfTree.left)
        pLeftTree = pRootOfTree.left
 
        # 连接根与左子树最大结点
        if pLeftTree:
            while(pLeftTree.right):
                pLeftTree = pLeftTree.right
            pRootOfTree.left, pLeftTree.right = pLeftTree, pRootOfTree
 
        # 处理右子树
        self.Convert(pRootOfTree.right)
        pRightTree = pRootOfTree.right
 
        # 连接根与右子树最小结点
        if pRightTree:
            while(pRightTree.left):
                pRightTree = pRightTree.left
            pRootOfTree.right, pRightTree.left = pRightTree, pRootOfTree
             
        while(pRootOfTree.left):
            pRootOfTree = pRootOfTree.left
        return pRootOfTree
