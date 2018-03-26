# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not m or not n:
            return -1

        res = range(n)

        i = 0
        while len(res) > 1:
            i = (m + i - 1) % len(res)
            res.pop(i)
        return res[0]
        '''
        if n == 0:
            return -1
        if n == 1:
            return 0
        else:
            return (self.LastRemaining_Solution(n-1, m) + m) % n
        '''
