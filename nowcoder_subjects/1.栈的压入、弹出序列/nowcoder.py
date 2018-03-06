# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        tempV = []
        while pushV:
            tempV.insert(0, pushV[0])
            pushV.pop(0)
            if popV[0] == tempV[0]:
                tempV.pop(0)
                popV.pop(0)

        if not tempV or tempV == popV:
            return True
        return False


s = Solution()
print s.IsPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 2, 1])

'''
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        return True
'''
