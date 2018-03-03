# -*- coding:utf-8 -*-
from collections import deque


class Solution:
    def reOrderArray(self, array):
        # write code here
        res = deque([])
        lenth = len(array)
        for i in range(lenth-1, -1, -1):
            if array[i] % 2 == 1:
                res.appendleft(array[i])
        for i in range(lenth):
            if array[i] % 2 == 0:
                res.append(array[i])
        return res

s = Solution()
s.reOrderArray([1, 2, 3, 4, 5, 6, 7])
