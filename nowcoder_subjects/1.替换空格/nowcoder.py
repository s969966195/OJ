# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        res = s.replace(' ', '%20')
        return res

s = Solution()
print s.replaceSpace("We Are Happy")
