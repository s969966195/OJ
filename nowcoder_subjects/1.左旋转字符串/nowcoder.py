# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        return s[n:]+s[:n]


s = Solution()
print s.LeftRotateString('abcdefg', 2)
