# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        return sum([(n >> i) & 1 for i in range(32)])


s = Solution()
s.NumberOf1(-1)
